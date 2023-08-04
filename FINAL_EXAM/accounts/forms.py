from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from FINAL_EXAM.kids.models import Kid

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


class AppUserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture', 'gender']

        labels = {
            'username': 'Username:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'email': 'Email:',
            'profile_picture': 'Image:',
            'gender': 'Gender:',
        }


class FilterKidsForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = [('', 'All kids')]  # Placeholder choice
        choices += [(kid.id, kid) for kid in Kid.objects.filter(user=user)]
        self.fields['filter_by_kid_name'] = forms.ChoiceField(
            choices=choices,
            required=False,
            widget=forms.Select(attrs={'onchange': 'this.form.submit();'})
        )
