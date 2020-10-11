from project.lists import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.lists_all, name="lists_all"),
    url(r'(?P<list_name>.*)/$', views.list_detail, name="list_detail"),
]
