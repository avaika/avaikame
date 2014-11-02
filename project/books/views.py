# from django.http import Http404
# from django.shortcuts import render, get_object_or_404
# from django.views.generic import RedirectView, TemplateView, DetailView, ListView
from django.views.generic import ListView
from models import Book

# from django.contrib.auth import get_user_model
# User = get_user_model()


class BookListView(ListView):
    # queryset = Book.objects.all
    model = Book
    paginate_by = 100
    context_object_name = "books"
    template_name = 'books/list.html'

book_main = BookListView.as_view()
