from django.contrib import admin

from .models import Casa


class CasaAdmin(admin.ModelAdmin):
    list_display = ('valor', 'endereco', 'donos')



admin.site.register(Casa, CasaAdmin)