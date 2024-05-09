from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label='Name', max_length=10)
    check = forms.BooleanField()

class CreateLocation(forms.Form):
    locationName = forms.CharField(label='Location', min_length=5, max_length=100)

