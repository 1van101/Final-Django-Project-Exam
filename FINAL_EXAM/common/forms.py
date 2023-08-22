from django import forms

from FINAL_EXAM.common.models import Comment


class SearchForm(forms.Form):
    drawings_of_searched_kid = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search drawing by kid name...'
            }
        )
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add comment...'})
        }
