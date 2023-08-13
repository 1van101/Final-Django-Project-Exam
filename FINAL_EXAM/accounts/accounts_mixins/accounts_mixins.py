from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render


class IsStaffOrOwnerAccountsMixin(UserPassesTestMixin):
    def test_func(self):
        requested_user = self.request.user
        object_user = self.get_object()
        return requested_user.is_staff or requested_user == object_user

    # def handle_no_permission(self):
    #     if self.request.user.is_authenticated:
    #         raise PermissionDenied
    #     else:
    #         return super().handle_no_permission()
