from rest_framework import permissions

class AnonymousPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return not(request.user and request.user.is_authenticated())
