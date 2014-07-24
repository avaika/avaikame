import urllib
import datetime

from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from project.adminfiles.models import FileUpload
from project.adminfiles import settings


class DisableView(Exception):
    pass


class BaseView(TemplateView):
    template_name = 'adminfiles/uploader/base.html'

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context.update({
            'browsers': get_enabled_browsers(),
            'field_id': self.request.GET['field'],
            'field_type': self.request.GET.get('field_type', 'textarea'),
            'ADMINFILES_REF_START': settings.ADMINFILES_REF_START,
            'ADMINFILES_REF_END': settings.ADMINFILES_REF_END,
            'JQUERY_URL': settings.JQUERY_URL
        })

        return context

    @classmethod
    def slug(cls):
        """
        Return slug suitable for accessing this view in a URLconf.

        """
        slug = cls.__name__.lower()
        if slug.endswith('view'):
            slug = slug[:-4]
        return slug

    @classmethod
    def link_text(cls):
        """
        Return link text for this view.

        """
        link = cls.__name__
        if link.endswith('View'):
            link = link[:-4]
        return link

    @classmethod
    def url(cls):
        """
        Return URL for this view.

        """
        return reverse('adminfiles_%s' % cls.slug())

    @classmethod
    def check(cls):
        """
        Raise ``DisableView`` if the configuration necessary for this
        view is not active.

        """
        pass


class AllView(BaseView):
    link_text = _('All Uploads')

    def files(self):
        return FileUpload.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AllView, self).get_context_data(**kwargs)
        now = datetime.datetime.now()
        earlier = now - datetime.timedelta(days=3)
        context.update({
            'files': self.files().filter(upload_date__gt=earlier).order_by(*settings.ADMINFILES_THUMB_ORDER)
        })
        return context


class ImagesView(AllView):
    link_text = _('Images')

    def files(self):
        now = datetime.datetime.now()
        earlier = now - datetime.timedelta(minutes=40)
        return super(ImagesView, self).files().filter(content_type='image', upload_date__gt=earlier)


class AudioView(AllView):
    link_text = _('Audio')

    def files(self):
        return super(AudioView, self).files().filter(content_type='audio')


class FilesView(AllView):
    link_text = _('Files')

    def files(self):
        not_files = ['video', 'image', 'audio']
        return super(FilesView, self).files().exclude(content_type__in=not_files)


def download(request):
    '''Saves image from URL and returns ID for use with AJAX script'''
    f = FileUpload()
    f.title = 'untitled'
    url = urllib.unquote(request.GET['photo'])
    file_content = urllib.urlopen(url).read()
    file_name = url.split('/')[-1]
    f.save_upload_file(file_name, file_content)
    f.save()
    return HttpResponse('%s' % (f.id))


_enabled_browsers_cache = None


def get_enabled_browsers():
    """
    Check the ADMINFILES_BROWSER_VIEWS setting and return a list of
    instantiated browser views that have the necessary
    dependencies/configuration to run.

    """
    global _enabled_browsers_cache
    if _enabled_browsers_cache is not None:
        return _enabled_browsers_cache
    enabled = []
    for browser_path in settings.ADMINFILES_BROWSER_VIEWS:
        try:
            view_class = import_browser(browser_path)
        except ImportError:
            continue
        if not issubclass(view_class, BaseView):
            continue
        browser = view_class
        try:
            browser.check()
        except DisableView:
            continue
        enabled.append(browser)
    _enabled_browsers_cache = enabled
    return enabled


def import_browser(path):
    module, classname = path.rsplit('.', 1)
    return getattr(__import__(module, {}, {}, [classname]), classname)
