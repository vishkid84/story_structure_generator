from django import forms
from .models import Story

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['name',
                  'overview',
                  'structure_one',
                  ]