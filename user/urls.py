# 子路由
from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^login/$', views.login),
]