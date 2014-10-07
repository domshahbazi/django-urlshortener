from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

from shorturl.models import urlObj
from shorturl.services import *
#shorten_url, lookup_url

# Create your views here.
def index(request):
    return render(request, 'shorturl/index.html')

def makeurl(request):
    # get url from form
    post_url = request.POST['url']

    # shorten the url and have the short code returned
    shortened_url = shorten_url(post_url)

    request.session['shortened_url'] = shortened_url

    return HttpResponseRedirect('create')
    
def create(request):
    shortened_url = request.session.get('shortened_url')
    return render(request, 'shorturl/create.html', {'shortened_url': shortened_url}) 

def redirect(request, short_url):
    url = lookup_url(short_url)
    return HttpResponseRedirect(url)

# Authenticate then authorize user login
def userlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index', args=[]))

    else:
        return HttpResponse('User doesnt exist')

# Log user out
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index', args=[]))
