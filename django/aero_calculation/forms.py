from django import forms

class AddForm(forms.Form):
    section = forms.CharField(max_length=40,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 't_v | c | l | v | K ', 'aria-describedby': 'add-btn'}))
