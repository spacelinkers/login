from django.urls import path,include, re_path

from accounts.views import(
    HomeView, LogInView, LogOutView, 
)

app_name = 'accounts'
urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^login/$', LogInView.as_view(), name = 'login'),
    re_path(r'^logout/$', LogOutView.as_view(), name='logout'),
     
]