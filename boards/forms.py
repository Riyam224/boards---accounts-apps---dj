from django import forms
from .models import Topic, Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(max_length=200, widget=forms.Textarea(attrs={
        'rows': '4',
        'placeholder': 'fill with cool message '
    }), help_text='max length is 200')

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['message']
