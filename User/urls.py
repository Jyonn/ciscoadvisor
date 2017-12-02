from django.conf.urls import url

from User.router import rt_user
from User.views import user_login

urlpatterns = [
    url(r'^$', rt_user),

    url(r'^login$', user_login),
]