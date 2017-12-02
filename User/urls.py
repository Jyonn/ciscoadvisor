from django.conf.urls import url

from User.router import rt_user
from User.views import user_login, user_logout

urlpatterns = [
    url(r'^$', rt_user),

    url(r'^login$', user_login),
    url(r'^logout$', user_logout),
]