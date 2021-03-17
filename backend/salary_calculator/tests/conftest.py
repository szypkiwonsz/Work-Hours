import datetime

import pytest

from salary_calculator.models import Year, Month, Day, Salary, Payout

from users.models import User


# fixtures for test_models
@pytest.fixture()
def user(db):
    user = User.objects.create(
        email='test@email.com',
        password='test_password'
    )
    return user


@pytest.fixture()
def year(user):
    year = Year.objects.create(
        user=user,
        name=2021
    )
    return year


@pytest.fixture()
def month(user, year):
    month = Month.objects.create(
        user=user,
        year=year,
        name='march'
    )
    return month


@pytest.fixture()
def salary(user):
    salary = Salary.objects.create(
        user=user,
        hourly_earnings=15
    )
    return salary


@pytest.fixture()
def day(user, salary):
    day = Day.objects.create(
        user=user,
        date=datetime.date(year=2021, month=1, day=1),
        work_start_time=datetime.time(hour=8, minute=0),
        work_end_time=datetime.time(hour=16, minute=0),
        bonus=120
    )
    return day
