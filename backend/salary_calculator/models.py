import calendar

from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Year(models.Model):
    """Class representing the model of the year for retrieving information on earnings during the year."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=4)

    class Meta:
        unique_together = ('user', 'name',)  # only one year name can be assigned to a user

    def __str__(self):
        return f'{self.user}, {self.name}'


class Month(models.Model):
    """Class representing the model of the month for retrieving information on earnings during the month."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, blank=True, related_name='months')
    name = models.CharField(max_length=9)

    class Meta:
        unique_together = ('user', 'year', 'name',)  # only one year and month name can be assigned to a user

    def __str__(self):
        return f'{self.year}, {self.name}'

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()  # capitalizing month name
        super(Month, self).save(*args, **kwargs)


class Day(models.Model):
    """Class representing the model of the day for retrieving information on earnings during the day."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE, blank=True, related_name='days')
    date = models.DateField()
    work_start_time = models.TimeField()
    work_end_time = models.TimeField()
    bonus = models.FloatField(default=0, validators=[MinValueValidator(0.0)])  # extra money earned during the day
    work_time = models.PositiveIntegerField(blank=True, help_text='given in minutes')

    class Meta:
        unique_together = ('user', 'date',)  # only one day date can be assigned to a user

    def __str__(self):
        return f'{self.user}, {self.date}'

    def save(self, *args, **kwargs):
        # gets or creates an object when creating a Day object
        year, _ = Year.objects.get_or_create(user=self.user, name=self.get_year_name())
        self.month, _ = Month.objects.get_or_create(user=self.user, name=self.get_month_name(), year=year)
        # saves the calculated working hours
        self.work_time = self.calculate_work_time()
        self.bonus = round(self.bonus, 2)  # rounding the bonus to 2 decimal places
        super(Day, self).save(*args, **kwargs)

    def get_month_name(self):
        """
        Gets month name from date of day object created.
        :return: <str> -> month name
        """
        month_number = str(self.date).split('-')[1].lstrip('0')
        month_name = calendar.month_name[int(month_number)]
        return month_name

    def get_year_name(self):
        """
        Gets year name from date of day object created.
        :return: <str> -> year name
        """
        year_name = str(self.date).split('-')[0]
        return year_name

    def calculate_work_time(self):
        """
        Calculates work time of day work hours
        :return: <int> -> working hours in minutes
        """
        work_hours = (self.work_end_time.hour - self.work_start_time.hour)
        work_minutes = (self.work_end_time.minute - self.work_start_time.minute)
        return work_hours * 60 + work_minutes


class Salary(models.Model):
    """Class representing the earnings assigned to the selected user."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hourly_earnings = models.PositiveIntegerField()
    hourly_earnings_saturdays = models.PositiveIntegerField(default=0)
    hourly_earnings_sundays = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Salaries'

    def __str__(self):
        return f'{self.user} salary'


class Payout(models.Model):
    """Class representing the payout for a given user in the selected month."""
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    month = models.OneToOneField(Month, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monthly_earnings = models.FloatField(default=0, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f'{self.month} payout'

    def save(self, *args, **kwargs):
        # saves the calculated monthly earnings
        self.monthly_earnings = self.calculate_monthly_earnings()
        super(Payout, self).save(*args, **kwargs)

    def calculate_monthly_earnings(self):
        """Calculates all the user's earnings for a given month."""
        monthly_bonus = sum(list(self.month.days.values_list('bonus', flat=True)))
        monthly_work_time = sum(list(self.month.days.values_list('work_time', flat=True)))
        # rounding monthly earnings to 2 decimal places
        return round(monthly_work_time / 60 * self.user.salary.hourly_earnings + monthly_bonus, 2)
