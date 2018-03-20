from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = 'workouts'

urlpatterns = [
    
    url(r'^Home/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='description'),
    url(r'^(?P<User_ID>[0-9]+)/user/$', views.workout_summary, name='summary'),
]
