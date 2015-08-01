from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.template.context import RequestContext
from django.views.generic import ListView

@csrf_exempt
def login(request):  
    return render_to_response('login.html',context_instance=RequestContext(request))

@csrf_exempt    
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/books')
    else:
        return render_to_response('login.html',{'error':'wrong username or password'},context_instance=RequestContext(request))
