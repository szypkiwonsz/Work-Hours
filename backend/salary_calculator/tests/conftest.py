import datetime

import pytest
from django.contrib.auth.models import AnonymousUser
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory

from salary_calculator.models import Year, Month, Day
from salary_calculator.serializers import DaySerializer, SalarySerializer, PayoutSerializer
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
def day(user):
    day = Day.objects.create(
        user=user,
        date=datetime.date(year=2021, month=1, day=1),
        work_start_time=datetime.time(hour=8, minute=0),
        work_end_time=datetime.time(hour=16, minute=0),
        bonus=120
    )
    return day


# fixtures for test_serializers
@pytest.fixture()
def day_serializer_data():
    day_serializer_data = {
        'id': 1,
        'date': '2021-01-01',
        'work_start_time': '08:00:00',
        'work_end_time': '16:00:00',
        'bonus': 0.0,
        'work_time': 480
    }
    return day_serializer_data


@pytest.fixture()
def day_serializer(day_serializer_data):
    factory = APIRequestFactory()
    request = factory.post(reverse('days-list', kwargs={'month_name': 'january'}))
    request.user = AnonymousUser()
    return DaySerializer(data=day_serializer_data, context={'request': request})


@pytest.fixture()
def salary_serializer_data():
    salary_serializer_data = {
        'hourly_earnings': 15,
        'hourly_earnings_saturdays': 0,
        'hourly_earnings_sundays': 0
    }
    return salary_serializer_data


@pytest.fixture()
def salary_serializer(salary_serializer_data):
    return SalarySerializer(data=salary_serializer_data)


@pytest.fixture()
def payout_serializer_data():
    payout_serializer_data = {
        'monthly_earnings': 2000
    }
    return payout_serializer_data


@pytest.fixture()
def payout_serializer(payout_serializer_data):
    return PayoutSerializer(data=payout_serializer_data)
