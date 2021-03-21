from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Custom permission class that allows to manage the object if the logged user is the owner of the object."""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
