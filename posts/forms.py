from django import forms
from .models import *
# from .models import BlogPost, Category


class BlogForm(forms.ModelForm):

    title = forms.CharField(
        label="Blog post title",
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the title of your blog post......'
        })
    )

    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={
            'placeholder': 'Write your blog post here......'
        })
    )

    image = forms.ImageField(
        label='Upload an Image',
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    category = forms.ModelChoiceField(
        queryset = Category.objects.all(),
        required=False,
        label = 'Select Category',
        widget = forms.Select()
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        label="Select Tags",
        widget=forms.SelectMultiple()
    )

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'category', 'tags']