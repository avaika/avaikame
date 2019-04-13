from django.views.generic import ListView
from models import Book


class BookListView(ListView):
    # somehow with postgres django returns duplicate entries without
    # defined queryset. need to investigate why it happens
    # works fine with mysql though...
    Book.objects.filter(active=True).order_by('-created')
    model = Book
    paginate_by = 100
    context_object_name = "books"
    template_name = 'books/list.html'

book_main = BookListView.as_view()
