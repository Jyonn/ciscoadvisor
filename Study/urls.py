from django.conf.urls import url

from Study.router import rt_study

urlpatterns = [
    url(r'^$', rt_study),
]