from django.conf.urls import url

from Study.router import rt_study, rt_study_trail_req, rt_study_trail_resp

urlpatterns = [
    url(r'^$', rt_study),
    url(r'^trail/request$', rt_study_trail_req),
    url(r'^trail/response$', rt_study_trail_resp),
]