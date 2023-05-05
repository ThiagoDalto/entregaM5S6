from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import User
from rest_framework.views import View
import ipdb


class IsSuperuser(BasePermission):
    # def has_object_permission(self, request, view: View, obj: User) -> bool:
    #     return request.user.is_superuser
    def has_permission(self, request, view):
        if request.method in "POST":
            return True
        return (request.user.is_authenticated and request.user.is_superuser)
