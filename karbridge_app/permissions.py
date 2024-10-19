from rest_framework import permissions

class IsKarfarma(permissions.BasePermission):
    """
    مجوز برای کارفرما
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.karfarma.user

    def has_permission(self, request, view):
        return request.user.role == 'karfarma'

class IsKarjo(permissions.BasePermission):
    """
    مجوز برای کارجو
    """

    def has_permission(self, request, view):
        return request.user.role == 'karjo'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.karjo.user
