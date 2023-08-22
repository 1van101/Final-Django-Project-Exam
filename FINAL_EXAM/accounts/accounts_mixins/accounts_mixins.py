from django.contrib.auth.mixins import UserPassesTestMixin


class IsStaffOrOwnerAccountsMixin(UserPassesTestMixin):
    def test_func(self):
        requested_user = self.request.user
        object_user = self.get_object()
        return requested_user.is_staff or requested_user == object_user
