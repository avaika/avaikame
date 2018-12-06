from django.views.generic import ListView
from models import List, Entry


class ListListView(ListView):
    List.objects.all().order_by('-created')
    model = List
    paginate_by = 100
    context_object_name = "lists"
    template_name = 'lists/list.html'


lists_main = ListListView.as_view()
