from project.lists import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.lists_all, name="lists_all"),
    re_path(r'(?P<list_name>.*)/$', views.list_detail, name="list_detail"),
]
