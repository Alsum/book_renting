from django import forms 
from models import Book


class BookForm(forms.ModelForm):
    
    class Meta:
        model=Book
        fields = ('title', 'isbn','author_name','edition_number',
        		'publication_date','status','fees','link')