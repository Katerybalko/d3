from django import forms
from .models import Post
from django.core.exceptions import ValidationError
class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)
    class Meta:
       model = Post
       fields = [
           'title',
           'category',
           'author',
           'text',
       ]
       def clean(self):
           cleaned_data = super().clean()
           name = cleaned_data.get("title")
           description = cleaned_data.get("text")
           if name == description:
               raise ValidationError(
                   "Текст не должен быть идентичен названию."
               )
           return cleaned_data

