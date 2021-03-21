import pytest

from salary_calculator.models import Payout


@pytest.mark.salary_calculator_signals
class TestSignals:

    def test_update_payout_monthly_earnings(self, day):
        day.bonus = 140
        day.save()
        payout = Payout.objects.get(month=day.month)
        assert payout.monthly_earnings == 260

    def test_remove_payout_monthly_earnings(self, day):
        day.delete()
        payout = Payout.objects.get(month=day.month)
        assert payout.monthly_earnings == 0.0
