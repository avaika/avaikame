from django.views.generic import ListView
from models import Book


class BookListView(ListView):
    # queryset = Book.objects.all
    model = Book
    paginate_by = 100
    context_object_name = "books"
    template_name = 'books/list.html'

book_main = BookListView.as_view()
