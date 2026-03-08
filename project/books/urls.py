from project.books import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.book_main, name="books"),
]
