from project.blog import views
from django.conf.urls import url, patterns

urlpatterns = patterns(
    '',
    url(r'^$', views.main),
    url(r'^page/(?P<pk>[0-9]+)/$', views.page_redirect, name='page_redirect'),
    url(r'^page/(?P<pk>[0-9]+)/(?P<slug>.*)/$', views.page_display, name='page_display'),
    url(r'^directions/(?P<post>[0-9]+)/$', views.directions, name='directions'),
    # url(r'^contacts/$', views.contact, name='contacts'),
    # url(r'^contacts/thanks/$', views.contact_thank, name='contacts_thanks'),
)
