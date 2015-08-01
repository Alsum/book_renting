from django.conf.urls.defaults import patterns, url
from models import  User
from django.conf import settings
from views import BookList
import views

urlpatterns = patterns('',
                       url(r'^$',BookList.as_view()),
                       url(r'^new/$',views.new,name="new_book"),
                       url(r'^search/$',views.book_search,name="book_search"),  
)
