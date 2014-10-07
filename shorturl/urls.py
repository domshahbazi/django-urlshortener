from django.conf.urls import patterns, url

from shorturl import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),                 
    url(r'^makeurl$', views.makeurl, name='makeurl'),
    url(r'^userlogin$', views.userlogin, name='userlogin'),
    url(r'^userlogout$', views.userlogout, name='userlogout'),
    # URL to match short code
    url(r'^(?P<short_url>.{6})$', views.redirect, name='redirect'),
)
