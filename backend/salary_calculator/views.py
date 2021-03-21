from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from salary_calculator.models import Salary, Payout
from salary_calculator.serializers import DaySerializer, SalarySerializer, PayoutSerializer
from salary_calculator.utils.mixins import MultipleFieldLookupMixin
from salary_calculator.utils.permissions import IsOwner


class DayViewSet(viewsets.ModelViewSet):
    """ViewSet for the Day model, enabling complete object management for the logged user who owns the object."""
    serializer_class = DaySerializer
    permission_classes = [IsOwner, IsAuthenticated]

    def get_queryset(self):
        """Displays the list of days from selected month assigned to the user."""
        month_name = self.kwargs['month_name'].capitalize()  # get month name from url kwargs
        return self.request.user.days.filter(month__name=month_name)


class SalaryView(generics.RetrieveUpdateAPIView):
    """ViewSet for the Salary model, enabling retrieving and updating object for the logged user who owns the object."""
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [IsOwner, IsAuthenticated]
    lookup_field = 'user__email'


class PayoutView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    """ViewSet for the Salary model, enabling retrieving object for the logged user who owns the object."""
    queryset = Payout.objects.all()
    serializer_class = PayoutSerializer
    permission_classes = [IsOwner, IsAuthenticated]
    lookup_fields = ['user__email', 'month__name']
