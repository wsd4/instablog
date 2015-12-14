from django import forms

from .models import Post


class PostNormalForm(forms.Form):

    title = forms.CharField()
    content = forms.CharField(
            widget=forms.Textarea
    )
    category = forms.IntegerField()
