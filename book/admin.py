from django.contrib import admin
from models import Book

class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'isbn', 'author_name',
    	      'edition_number','publication_date',
    	      'status','fees','link','renter')
    list_display = ('title','isbn')
    search_fields=('title','isbn')
    
    

admin.site.register(Book,BookAdmin)