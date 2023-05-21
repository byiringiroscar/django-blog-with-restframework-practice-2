from django import forms
from .models import *


class SportForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = ['name', 'position', 'team', 'country', 'description', 'goals', 'assists', 'player_image']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'body']
