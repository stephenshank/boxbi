from django.contrib import admin

from api.models import PLC


class PLCAdmin(admin.ModelAdmin):
    list_display = ('plc_id', 'name', 'tag')


admin.site.register(PLC, PLCAdmin)
