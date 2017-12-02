from django.conf.urls import url

from Study.router import rt_study, rt_study_trail

urlpatterns = [
    url(r'^$', rt_study),
    url(r'^trail$', rt_study_trail)
]