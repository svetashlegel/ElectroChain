from rest_framework import permissions


class IsActiveUserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_active
