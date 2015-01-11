from project.books import views
from django.conf.urls import url, patterns

urlpatterns = patterns(
    '',
    url(r'^$', views.book_main, name="books"),
)
