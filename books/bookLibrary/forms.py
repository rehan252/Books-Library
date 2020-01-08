from django import forms
from .models import Book


class BookUpload(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Book
        fields = '__all__'


