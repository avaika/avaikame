from project.lists import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.lists_main, name="lists_all"),
]
