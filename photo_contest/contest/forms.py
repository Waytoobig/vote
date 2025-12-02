from django import forms
from .models import Candidate, Vote

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['voter_name', 'candidate']
        widgets = {
            'voter_name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'candidate': forms.RadioSelect(),  # use radio buttons for candidates
        }
