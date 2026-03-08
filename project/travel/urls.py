from project.travel import views
from django.urls import re_path
from django.views.generic import RedirectView

urlpatterns = [
    re_path(r'^$', views.category, name='travel_list'),
    re_path(r'^me/', RedirectView.as_view(url='/i/', query_string=True, permanent=True)),
    re_path(r'^page/(?P<pk>[0-9]+)/$', views.page_redirect, name='page_redirect'),
    re_path(r'^tag/(?P<tag>.*)/$', views.tag, name='tag_list'),
    re_path(r'^country/(?P<country>.*)/$', views.country_redirect, name='country_list'),
    re_path(r'^page/(?P<pk>[0-9]+)/(?P<slug>.*)/$', views.page_display, name='page_display'),
    re_path(r'^balls/$', views.balls, name='balls'),
]
