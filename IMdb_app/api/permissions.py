from rest_framework import permissions
from IMdb_app.models import Review

class AdminorReadonly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return (request.method == "GET")
        else:
            return bool(request.user and request.user.is_staff)


class object_permission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return Review.user == request.user or request.user.is_admin