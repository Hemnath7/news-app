from django import forms
from .models import Comment

# Forms
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment", )