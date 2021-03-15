from django.contrib import admin

from salary_calculator.models import Day, Salary, Month, Payout, Year

admin.site.register(Day)
admin.site.register(Salary)
admin.site.register(Month)
admin.site.register(Payout)
admin.site.register(Year)
