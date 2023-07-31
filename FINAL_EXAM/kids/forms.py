from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from FINAL_EXAM.kids.models import Kid


class AddKidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = '__all__'
        exclude = ('user', )
        widgets = {
            'date_of_birth': AdminDateWidget(),
        }