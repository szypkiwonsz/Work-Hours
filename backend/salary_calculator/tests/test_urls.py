import pytest
from django.urls import resolve, reverse

from salary_calculator.views import SalaryView, PayoutView


@pytest.mark.salary_calculator_urls
class TestUrls:

    def test_salary_url(self):
        url = resolve(reverse('salary', args=['test@email.com']))
        assert url.func.view_class == SalaryView

    def test_payout_url(self):
        url = resolve(reverse('payout', args=['test@email.com', 'march']))
        assert url.func.view_class == PayoutView
