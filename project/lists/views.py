from django.views.generic import ListView
from models import List, Entry


class AllListsView(ListView):
    List.objects.all().order_by('-created')
    model = List
    paginate_by = 100
    context_object_name = "lists"
    template_name = 'lists/list.html'


lists_all = AllListsView.as_view()


class ListDetailView(ListView):
    model = Entry
    paginate_by = 100
    context_object_name = "items"
    template_name = 'lists/item.html'

    def get_queryset(self):
        qs = super(ListDetailView, self).get_queryset()
        return qs.filter(listItem=kwargs['list_name'], published=True)

list_detail = ListDetailView.as_view()
