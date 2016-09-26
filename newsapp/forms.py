from django import forms

from newsapp.models import Feed

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ('url',)
