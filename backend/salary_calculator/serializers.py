from rest_framework import serializers

from salary_calculator.models import Day, Salary, Payout


class DaySerializer(serializers.ModelSerializer):
    """Serializer for the Day model."""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())  # saving the owner as the logged in user

    class Meta:
        model = Day
        fields = ['id', 'user', 'date', 'work_start_time', 'work_end_time', 'bonus', 'work_time']


class SalarySerializer(serializers.ModelSerializer):
    """Serializer for the Salary model."""

    class Meta:
        model = Salary
        fields = ['id', 'hourly_earnings', 'hourly_earnings_saturdays', 'hourly_earnings_sundays']


class PayoutSerializer(serializers.ModelSerializer):
    """Serializer for the Payout model."""

    class Meta:
        model = Payout
        fields = ['id', 'monthly_earnings']
