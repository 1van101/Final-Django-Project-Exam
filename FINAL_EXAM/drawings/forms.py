from django import forms
from django.contrib.auth import get_user_model

from FINAL_EXAM.drawings.models import Drawing
from FINAL_EXAM.kids.models import Kid

UserModel = get_user_model()


class DrawingForm(forms.ModelForm):
    class Meta:
        model = Drawing
        fields = ['drawing', 'description', 'kid_owner_drawing']

    def __init__(self, user, *args, **kwargs):
        super(DrawingForm, self).__init__(*args, **kwargs)
        # self.fields['kid_owner_drawing'].required = False

        if user.is_staff:
            self.fields['kid_owner_drawing'].queryset = Kid.objects.all()
        else:
            self.fields['kid_owner_drawing'].queryset = Kid.objects.filter(user=user)