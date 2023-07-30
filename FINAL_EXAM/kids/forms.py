from django import forms

from FINAL_EXAM.kids.models import Kid


class AddKidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = '__all__'
        exclude = ('user', )