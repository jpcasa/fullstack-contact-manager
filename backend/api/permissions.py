from rest_framework.permissions import BasePermission
from . import models


class IsOwnerAddress(BasePermission):
    """Custom permission to allow address editing"""

    def has_object_permission(self, request, view, obj):
        """Return true if permission is granted to owner."""
        if isinstance(obj, models.Address):
            return obj.owner == request.user
        return obj.owner == request.user


class isOwnerPhoneNumber(BasePermission):
    """Custom permission to allow phone editing"""

    def has_object_permission(self, request, view, obj):
        """Return true if permission is granted to owner."""
        if isinstance(obj, models.PhoneNumber):
            return obj.owner == request.user
        return obj.owner == request.user


class isOwnerEmail(BasePermission):
    """Custom permission to allow email editing"""

    def has_object_permission(self, request, view, obj):
        """Return true if permission is granted to owner."""
        if isinstance(obj, models.Email):
            return obj.owner == request.user
        return obj.owner == request.user


class IsOwnerContact(BasePermission):
    """Custom permission to allow contact editing"""

    def has_object_permission(self, request, view, obj):
        """Return true if permission is granted to owner."""
        if isinstance(obj, models.Contact):
            return obj.owner == request.user
        return obj.owner == request.user
