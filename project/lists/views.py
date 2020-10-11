from django.views.generic import ListView
from models import List, Entry


class AllListsView(ListView):
    List.objects.filter(published=True).order_by('-created')
    model = List
    paginate_by = 100
    context_object_name = "lists"
    template_name = 'lists/list.html'


lists_all = AllListsView.as_view()


class ListDetailView(ListView):
    model = Entry
    paginate_by = 100
    context_object_name = "items"
    template_name = 'lists/default.html'

    def get_queryset(self):
        qs = super(ListDetailView, self).get_queryset()
        return qs.filter(listItem__slug=self.kwargs['list_name'],
                listItem__published=True,
                published=True)

    def get_context_data(self, **kwargs):
        context = super(ListDetailView, self).get_context_data(**kwargs)
        context['current_list'] = List.objects.filter(slug=self.kwargs['list_name']).first()
        return context

list_detail = ListDetailView.as_view()
