from django import forms
from .models import Book, Author


class ProductForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title','genre','author', 'price', 'description', 'added')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        authors = Author.objects.all()
        names = [(a.id, a.get_name()) for a in authors]

        self.fields['author'].choices = names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'



class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name','info','books_written', 'image_url',)

