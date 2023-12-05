from django.contrib.auth import get_user_model
from rest_framework.permissions import SAFE_METHODS, BasePermission

User = get_user_model()


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        is_admin = bool(hasattr(request.user, 'role')
                        and request.user.is_admin)
        return is_admin

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsAdminUserOrReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return super().has_permission(request, view)


class ModeratorUser(BasePermission):
    def has_permission(self, request, view):
        return bool(hasattr(request.user, 'role')
                    and request.user.is_moderator)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            or request.user and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or obj.author == request.user)
