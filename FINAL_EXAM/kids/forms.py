from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth import get_user_model

from FINAL_EXAM.kids.models import Kid

UserModel = get_user_model()

class AddKidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Remove 'user' from kwargs if present
        super().__init__(*args, **kwargs)

        if user and not user.is_staff:
            self.fields.pop('user')


class KidEditForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['name', 'personal_photo']

        labels = {
            'name': 'Kid name:',
            'personal_photo': 'Kid photo:',
        }