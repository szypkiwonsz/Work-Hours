import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, force_authenticate

from salary_calculator.views import DayViewSet


@pytest.mark.salary_calculator_views
class TestDayViewSet:

    def test_get_list(self, user, day):
        kwargs = {'month_name': 'january'}
        factory = APIRequestFactory()
        request = factory.get(reverse('days-list', kwargs=kwargs))
        force_authenticate(request, user)
        view = DayViewSet.as_view({'get': 'list'})
        response = view(request, month_name=kwargs['month_name'])
        assert response.status_code == 200

    def test_post_list(self, user):
        kwargs = {'month_name': 'january'}
        day_data = {
            'date': '2021-01-01',
            'work_start_time': '08:00:00',
            'work_end_time': '16:00:00'
        }
        factory = APIRequestFactory()
        request = factory.post(reverse('days-list', kwargs=kwargs), day_data)
        force_authenticate(request, user)
        view = DayViewSet.as_view({'post': 'create'})
        response = view(request, month_name=kwargs['month_name'])
        assert response.status_code == 201

    def test_get_detail(self, user, day):
        kwargs = {'month_name': 'january', 'pk': 1}
        factory = APIRequestFactory()
        request = factory.get(reverse('days-detail', kwargs=kwargs))
        force_authenticate(request, user)
        view = DayViewSet.as_view({'get': 'retrieve'})
        response = view(request, month_name=kwargs['month_name'], pk=kwargs['pk'])
        assert response.status_code == 200

    def test_put_detail(self, user, day):
        kwargs = {'month_name': 'january', 'pk': 1}
        day_data = {
            'date': '2021-01-01',
            'work_start_time': '08:00:00',
            'work_end_time': '16:00:00'
        }
        factory = APIRequestFactory()
        request = factory.put(reverse('days-detail', kwargs=kwargs), day_data)
        force_authenticate(request, user)
        view = DayViewSet.as_view({'put': 'update'})
        response = view(request, month_name=kwargs['month_name'], pk=kwargs['pk'])
        assert response.status_code == 200

    def test_delete_detail(self, user, day):
        kwargs = {'month_name': 'january', 'pk': 1}
        factory = APIRequestFactory()
        request = factory.delete(reverse('days-detail', kwargs=kwargs))
        force_authenticate(request, user)
        view = DayViewSet.as_view({'delete': 'destroy'})
        response = view(request, month_name=kwargs['month_name'], pk=kwargs['pk'])
        assert response.status_code == 204
