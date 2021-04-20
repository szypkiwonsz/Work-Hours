import pytest


@pytest.mark.salary_calculator_serializers
class TestDaySerializer:

    def test_contains_expected_fields(self, day_serializer):
        day_serializer.is_valid()
        assert set(day_serializer.data.keys()) == {'date', 'work_start_time', 'work_end_time', 'bonus',
                                                   'work_time'}

    def test_fields_content(self, day_serializer):
        day_serializer.is_valid()
        assert day_serializer.data['date'] == '2021-01-01'
        assert day_serializer.data['work_start_time'] == '08:00:00'
        assert day_serializer.data['work_end_time'] == '16:00:00'
        assert day_serializer.data['bonus'] == 0.0
        assert day_serializer.data['work_time'] == 480


@pytest.mark.salary_calculator_serializers
class TestSalarySerializer:

    def test_contains_expected_fields(self, salary_serializer):
        salary_serializer.is_valid()
        assert set(salary_serializer.data.keys()) == {'hourly_earnings', 'hourly_earnings_saturdays',
                                                      'hourly_earnings_sundays'}

    def test_fields_content(self, salary_serializer):
        salary_serializer.is_valid()
        assert salary_serializer.data['hourly_earnings'] == 15
        assert salary_serializer.data['hourly_earnings_saturdays'] == 0
        assert salary_serializer.data['hourly_earnings_sundays'] == 0


@pytest.mark.salary_calculator_serializers
class TestPayoutSerializer:

    def test_contains_expected_fields(self, payout_serializer):
        payout_serializer.is_valid()
        assert set(payout_serializer.data.keys()) == {'monthly_earnings'}

    def test_fields_content(self, payout_serializer):
        payout_serializer.is_valid()
        assert payout_serializer.data['monthly_earnings'] == 2000
