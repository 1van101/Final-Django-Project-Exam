from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from FINAL_EXAM.kids.models import Kid


class AddKidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = '__all__'
        exclude = ('user',)


class KidEditForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['name', 'personal_photo']

        labels = {
            'name': 'Kid name:',
            'personal_photo': 'Kid photo:',
        }