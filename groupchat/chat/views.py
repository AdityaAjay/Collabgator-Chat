import json
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from django.http import JsonResponse
from login import views
from django.http import HttpResponse


def user_list(request):
    if views.signedIn:
        return render(request, 'chat/user_list.html')
    else:
        return HttpResponse("""
                <script type="text/javascript">
                alert('Please sign in')
                window.location.href = "/signin"    
                </script>""")
