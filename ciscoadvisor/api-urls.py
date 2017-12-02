from django.conf.urls import url, include

urlpatterns = [
    url(r'^user/', include('User.urls')),
    url(r'^algo/', include('Algorithm.urls')),
    url(r'^study/', include('Study.urls')),
]