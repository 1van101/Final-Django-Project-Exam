from django import forms



class SearchForm(forms.Form):
    drawings_of_searched_kid = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search drawing by kid name...'
            }
        )
    )