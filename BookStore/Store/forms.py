from django import forms


class BookForm(forms.Form):
    description = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'description', 'class': "form-control text-center"}), max_length=500, required=True)
    file = forms.FileField()


    tags = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'tags with - ', 'class': "form-control text-center"}), max_length=500, required=True)