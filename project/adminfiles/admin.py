from django.http import HttpResponse

from django.contrib import admin

from project.adminfiles.models import FileUpload
from project.adminfiles.settings import JQUERY_URL
from project.adminfiles.listeners import register_listeners
from multiupload.admin import MultiUploadAdmin


class FileUploadAdmin(MultiUploadAdmin):
    change_form_template = 'multiupload/change_form.html'
    change_list_template = 'multiupload/change_list.html'
    multiupload_template = 'multiupload/upload.html'
    multiupload_list = True
    multiupload_form = True
    multiupload_acceptedformats = ("image/jpeg",
                                   "image/png",)
    list_display = ['upload_date', 'upload', 'mime_type']

    # uncomment for snipshot photo editing feature
    # class Media:
    #    js = (JQUERY_URL, 'adminfiles/photo-edit.js')

    def response_change(self, request, obj):
        if request.POST.has_key("_popup"):
            return HttpResponse('<script type="text/javascript">'
                                'opener.dismissEditPopup(window);'
                                '</script>')
        return super(FileUploadAdmin, self).response_change(request, obj)

    def delete_view(self, request, *args, **kwargs):
        response = super(FileUploadAdmin, self).delete_view(request,
                                                            *args,
                                                            **kwargs)
        if request.POST.has_key("post") and request.GET.has_key("_popup"):
            return HttpResponse('<script type="text/javascript">'
                                'opener.dismissEditPopup(window);'
                                '</script>')
        return response

    def response_add(self, request, *args, **kwargs):
        if request.POST.has_key('_popup'):
            return HttpResponse('<script type="text/javascript">'
                                'opener.dismissAddUploadPopup(window);'
                                '</script>')
        return super(FileUploadAdmin, self).response_add(request,
                                                         *args,
                                                         **kwargs)

    def process_uploaded_file(self, uploaded, object, **kwargs):
        f = self.model(upload=uploaded)
        f.save()
        return {'url': f.imagem(),
                'thumbnail_url': f.imagem(),
                'name': f.id,
                'id': f.id}


class FilePickerAdmin(admin.ModelAdmin):
    adminfiles_fields = []

    def __init__(self, *args, **kwargs):
        super(FilePickerAdmin, self).__init__(*args, **kwargs)
        register_listeners(self.model, self.adminfiles_fields)

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(FilePickerAdmin, self).formfield_for_dbfield(
            db_field, **kwargs)
        if db_field.name in self.adminfiles_fields:
            try:
                field.widget.attrs['class'] += " adminfilespicker"
            except KeyError:
                field.widget.attrs['class'] = 'adminfilespicker'
        return field

    class Media:
        js = [JQUERY_URL, 'https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=places', 'adminfiles/model.js', 'adminfiles/maps.js']

admin.site.register(FileUpload, FileUploadAdmin)
