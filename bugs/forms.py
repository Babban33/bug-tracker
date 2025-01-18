from django import forms
from .models import Bug

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['title', 'description', 'priority', 'assigned_to']

class BugSearchForm(forms.Form):
    search = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[('', 'All')] + Bug.STATUS_CHOICES, required=False)
    priority = forms.ChoiceField(choices=[('', 'All')] + Bug.PRIORITY_CHOICES, required=False)

