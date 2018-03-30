# todo/urls.py
from django.conf.urls import url
from todo import views

from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^accounts/profile/$', views.ProfilePageView.as_view(), name='todo-list'),
    url(r'^accounts/profile/clear/$', views.clear_resolved_todos, name='todo-clear'),
    url(r'^accounts/profile/toggle/$', views.toggle_todos, name='todos-toggle'),
    url(r'^accounts/profile/add/$', views.TodoCreateView.as_view(), name='todo-create'),
    url(r'^accounts/profile/toggle/(?P<todo_id>\d+)/$', views.toggle_todo, name='todo-toggle'),
    url(r'^accounts/profile/delete/(?P<pk>\d+)/$', views.TodoDeleteView.as_view(), name='todo-delete'),
]
