from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render


class IsStaffOrOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_staff or user == self.get_object())

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            # return render(self.request, '403.html', status=403)
            raise PermissionDenied
        else:
            return super().handle_no_permission()
