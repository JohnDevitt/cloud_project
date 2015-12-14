from django import forms

class MontageCreateForm(forms.Form):

    forms.CharField(label='Montage title', max_length=1000)
    file = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )