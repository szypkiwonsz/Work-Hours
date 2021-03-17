import pytest
from django.db import IntegrityError

from salary_calculator.models import Year, Month, Day


@pytest.mark.salary_calculator_models
class TestYear:

    def test_string_representation(self, year):
        assert str(year) == 'test@email.com, 2021'

    def test_unique_together(self, year):
        with pytest.raises(IntegrityError):
            Year.objects.create(
                user=year.user,
                name=year.name
            )


@pytest.mark.salary_calculator_models
class TestMonth:

    def test_string_representation(self, month):
        assert str(month) == 'test@email.com, 2021, March'

    def test_save(self, month):
        assert month.name == 'March'

    def test_unique_together(self, month):
        with pytest.raises(IntegrityError):
            Month.objects.create(
                user=month.user,
                year=month.year,
                name=month.name
            )


@pytest.mark.salary_calculator_models
class TestDay:

    def test_string_representation(self, day):
        assert str(day) == 'test@email.com, 2021-01-01'

    def test_save(self, day):
        assert day.month.name == 'January'
        assert day.bonus == 120
        assert day.work_time == 480

    def test_unique_together(self, day):
        with pytest.raises(IntegrityError):
            Day.objects.create(
                user=day.user,
                date=day.date,
                work_start_time=day.work_start_time,
                work_end_time=day.work_end_time,
                bonus=day.bonus
            )

    def test_get_month_name(self, day):
        assert day.get_month_name() == 'January'

    def test_get_year_name(self, day):
        assert day.get_year_name() == '2021'

    def test_calculate_work_time(self, day):
        assert day.calculate_work_time() == 480


@pytest.mark.salary_calculator_models
class TestSalary:

    def test_string_representation(self, salary):
        assert str(salary) == 'test@email.com salary'


@pytest.mark.salary_calculator_models
class TestPayout:
    """The day object automatically creates the month and the payout."""

    def test_string_representation(self, day):
        assert str(day.month.payout) == 'test@email.com, 2021, January payout'

    def test_save(self, day):
        assert day.month.payout.monthly_earnings == 240.0

    def test_calculate_monthly_earnings(self, day):
        assert day.month.payout.calculate_monthly_earnings() == 240.0
