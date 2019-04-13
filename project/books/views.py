from django.views.generic import ListView
from models import Book


class BookListView(ListView):
    model = Book
    paginate_by = 100
    context_object_name = "books"
    template_name = 'books/list.html'

    def get_queryset(self):
        qs = super(BookListView, self).get_queryset()
        return qs.filter(active=True).order_by('-created')

book_main = BookListView.as_view()
