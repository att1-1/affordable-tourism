# forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    author_name = forms.CharField(
        label='Ваше имя',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Иван Иванов'
        })
    )
    
    class Meta:
        model = Comment
        fields = ['author_name', 'text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Оставьте ваш комментарий...'
            })
        }