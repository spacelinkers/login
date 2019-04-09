from django.urls import path,include, re_path

from accounts.views import(
    LogInView, 
)

app_name = 'accounts'
urlpatterns = [
    re_path(r'^login/$', LogInView.as_view(), name = 'login'),
]