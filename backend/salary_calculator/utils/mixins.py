from rest_framework.generics import get_object_or_404


class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering based on a `lookup_fields` attribute,
    instead of the default single field filtering.
    """

    def get_object(self):
        queryset = self.get_queryset()  # get the base queryset
        queryset = self.filter_queryset(queryset)  # apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:  # ignore empty fields
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # lookup the object
        self.check_object_permissions(self.request, obj)
        return obj
