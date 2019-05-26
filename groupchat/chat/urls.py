from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse
from chat.views import user_list

def customhandler404(request):
    return HttpResponse('<a href="/signin">Invalid URL. Please try again.</a>')

urlpatterns = [
    url(r'', user_list),#chat is the open url which any one can use to chat with anyone
    url(r'$',user_list,name='user_list')
]
