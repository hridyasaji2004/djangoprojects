from django import forms



from book.models import Book

class bookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'



