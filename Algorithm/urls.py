from django.conf.urls import url

from Algorithm.router import rt_algo

urlpatterns = [
    url(r'^$', rt_algo),
]
