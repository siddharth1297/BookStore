from django import forms


class BookForm(forms.Form):
    #subject = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'subject', 'class': "form-control text-center"}), max_length=50, required=True)
    description = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'description', 'class': "form-control text-center"}), max_length=500, required=True)
    file = forms.FileField()

    tag_choice = (('', ''), ('Computer Architecture', 'Computer Architecture'), ('Operating System', 'Operating System'), ('Networking', 'Networking'), ('Distributed System', 'Distributed System'), ('Machine Learning', 'Machine Learning'), ('Deep Learning', 'Deep Learning'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Algorithm', 'Algorithm'), ('Theoretical CS', 'Theoretical CS'))
    tags = forms.MultipleChoiceField(label='', widget=forms.SelectMultiple(attrs={'class': 'js-example-basic-multiple', 'style': 'width: 100%'}), choices=tag_choice)