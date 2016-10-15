from project.travel import views
from django.conf.urls import url
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', views.category, name='travel_list'),
    url(r'^me/', RedirectView.as_view(url='/i/', query_string=True, permanent=True)),
    url(r'^page/(?P<pk>[0-9]+)/$', views.page_redirect, name='page_redirect'),
    url(r'^tag/(?P<tag>.*)/$', views.tag, name='tag_list'),
    url(r'^country/(?P<country>.*)/$', views.country_redirect, name='country_list'),
    url(r'^page/(?P<pk>[0-9]+)/(?P<slug>.*)/$', views.page_display, name='page_display'),
    url(r'^directions/(?P<post>[0-9]+)/$', views.directions, name='directions'),
    url(r'^balls/$', views.balls, name='balls'),
]
