from project.blog import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.all_posts, name='blog_all_posts'),
    url(r'^(?P<slug>[^/]*)/$', views.category, name='blog_category'),
    url(r'^tag/(?P<tag>.*)/$', views.tag, name='blog_tag_list'),
    url(r'^page/(?P<pk>[0-9]+)/$', views.page_redirect, name='blog_page_redirect'),
    url(r'^page/(?P<pk>[0-9]+)/(?P<slug>.*)/$', views.page_display, name='blog_page_display'),
]
