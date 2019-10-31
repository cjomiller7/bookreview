from django import forms
from .models import Rev


class RevForm(forms.ModelForm):
    class Meta:  # where we tell Django which model should be used to create this form
        model = Rev
        fields = ('title', 'author', 'price', 'genre', 'age', 'review')


## In Dvelopment
class BrowForm(forms.ModelForm):
    class Meta:  # where we tell Django which model should be used to create this form
        model = Rev
        fields = ('price', 'genre', 'age')
