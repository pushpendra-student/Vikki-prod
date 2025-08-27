from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # this SAFE_METHODS contain get,head,opation for admin to have it
        if request.method == permissions.SAFE_METHODS:
            return True  # anyone can access target view
        return bool(request.user and request.user.is_staff)
