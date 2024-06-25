from django import forms
from .models import Post, Category


class CategoryMultipleChoiceField(forms.MultipleChoiceField):
    widget = forms.CheckboxSelectMultiple

    def __init__(self, *args, **kwargs):
        super(CategoryMultipleChoiceField, self).__init__(*args, **kwargs)
        self.choices = Category.choices


class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    cover_image = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )
    contents = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    categories = CategoryMultipleChoiceField()

    class Meta:
        model = Post
        fields = ['title', 'cover_image', 'contents', 'categories']


class ContactForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=100)
    lastName = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)
