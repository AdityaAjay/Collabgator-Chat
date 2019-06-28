from django.conf.urls import url
from login.views import signIn

urlpatterns = [
    url('', signIn, name='Sign In')
]
