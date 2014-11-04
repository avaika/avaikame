import posixpath

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

JQUERY_URL = getattr(settings, 'JQUERY_URL',
                     '//ajax.googleapis.com/ajax/libs/jquery/1.4/jquery.min.js')

if JQUERY_URL and not ((':' in JQUERY_URL) or (JQUERY_URL.startswith('/'))):
    JQUERY_URL = posixpath.join(settings.STATIC_URL, JQUERY_URL)

ADMINFILES_UPLOAD_TO = getattr(settings, 'ADMINFILES_UPLOAD_TO', 'adminfiles')

ADMINFILES_THUMB_ORDER = getattr(settings, 'ADMINFILES_THUMB_ORDER',
                                 ('-upload_date',))

ADMINFILES_USE_SIGNALS = getattr(settings, 'ADMINFILES_USE_SIGNALS', False)

ADMINFILES_REF_START = getattr(settings, 'ADMINFILES_REF_START', '<<<')

ADMINFILES_REF_END = getattr(settings, 'ADMINFILES_REF_END', '>>>')

ADMINFILES_STRING_IF_NOT_FOUND = getattr(settings,
                                         'ADMINFILES_STRING_IF_NOT_FOUND',
                                         u'')

ADMINFILES_INSERT_LINKS = getattr(
    settings,
    'ADMINFILES_INSERT_LINKS',
    {'': [(_('Insert Link'), {})],
     'image': [(_('Insert normal'), {'type': 'normal'}),
               (_('Insert right'), {'type': 'normal',
                                    'class': 'pull-right'}),
               (_('Insert vertical'), {'type': 'vertical'}),
               (_('Insert vright'), {'type': 'vertical',
                                     'class': 'pull-right'}),
               (_('Insert panorama'), {'type': 'panorama'}),
               (_('Insert small'), {'type': 'small'}), ]
     },
    )

ADMINFILES_STDICON_SET = getattr(settings, 'ADMINFILES_STDICON_SET', None)

ADMINFILES_BROWSER_VIEWS = getattr(settings, 'ADMINFILES_BROWSER_VIEWS',
                                   ['project.adminfiles.views.AllView',
                                    'project.adminfiles.views.ImagesView',
                                    'project.adminfiles.views.AudioView',
                                    'project.adminfiles.views.FilesView', ])
