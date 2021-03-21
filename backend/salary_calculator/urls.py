from django.urls import path
from rest_framework import routers

from salary_calculator.views import DayViewSet, SalaryView, PayoutView

router = routers.SimpleRouter()
router.register(r'days/(?P<month_name>[^/.]+)', DayViewSet, basename='days')

urlpatterns = [
    path('salary/<str:user__email>/', SalaryView.as_view(), name='salary'),
    path('payout/<str:user__email>/<str:month__name>/', PayoutView.as_view(), name='payout')
]

urlpatterns += router.urls
