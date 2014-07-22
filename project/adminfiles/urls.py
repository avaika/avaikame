from django.conf.urls import patterns, url

from django.contrib.admin.views.decorators import staff_member_required

from project.adminfiles.views import download, get_enabled_browsers

urlpatterns = patterns(
    '',
    url(r'download/$', staff_member_required(download),
        name="adminfiles_download")
)

for browser in get_enabled_browsers():
    slug = browser.slug()
    urlpatterns += patterns(
        '',
        url('%s/$' % slug, browser.as_view(),
            name='adminfiles_%s' % slug))
