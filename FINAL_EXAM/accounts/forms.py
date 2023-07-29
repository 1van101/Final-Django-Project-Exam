from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class AppUserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'is_visitor')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_visitor'].label = "Are you a visitor only?"


class LoginForm(auth_forms.AuthenticationForm):
    error_messages = {
        'invalid_login': 'Please enter a correct username and password!',
    }