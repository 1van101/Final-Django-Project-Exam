from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render


class IsStaffOrOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_staff or user == self.get_object().user

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied
        else:
            return super().handle_no_permission()
        raise PermissionDenied
