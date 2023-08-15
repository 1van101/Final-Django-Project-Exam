from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class UserAppAdmin(auth_admin.UserAdmin):
    list_per_page = 20
