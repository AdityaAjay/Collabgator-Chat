"""groupchat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from login.views import *


# this function is being used to redirect all stray URLs to the sign in page
def redirect(request):
    return HttpResponse("""<meta http-equiv="refresh" content="0; url=http://example.com">
        <script type="text/javascript">
            window.location.href = "/signin"
        </script>""")


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^chat/', include('chat.urls', namespace='chat')),
    url(r'^signin/', signIn),
    url(r'^postsign/', postsign),
    url(r'^forgotpassword/', forgotpassword),
    url(r'^signup/', signUp, name='signup'),
    url(r'^postsignup/', postsignup, name='postsignup'),
    url(r'^logout/', logout, name='postsignup'),
    url(r'^roomselected', roomselected),

    url(r'^$', signIn)

]
