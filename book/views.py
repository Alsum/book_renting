from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.views.generic import ListView
from models import Book
from forms import BookForm
from django.db.models import Q

class BookList(ListView):
    model = Book
    template_name='books.html'

@login_required
@csrf_exempt
def new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.renter = request.user
            book.save()
            return HttpResponseRedirect('/books')
    else:
        form = BookForm()
    return render_to_response('new.html', {'form': form},context_instance=RequestContext(request))

def book_search(request):
    #import pdb;pdb.set_trace()
    if request.is_ajax():
        qe = request.GET.get( 'q' )
        if qe is not None:
            if qe.isdigit():
                results = Book.objects.filter(Q(isbn__exact=int(qe)))
            else:     
                results = Book.objects.filter(Q(title__icontains=qe) | Q(author_name__icontains=qe)) 
            return render_to_response( 'results.html',{'results': results })        