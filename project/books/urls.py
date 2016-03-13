from project.books import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.book_main, name="books"),
]
