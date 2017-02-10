from django.contrib import admin

from api.models import IP, PLC


class IPAdmin(admin.ModelAdmin):
    list_display = ('ip_id', 'name', 'description', 'address')


class PLCAdmin(admin.ModelAdmin):
    list_display = ('plc_id', 'ip', 'name', 'tag')


admin.site.register(IP, IPAdmin)
admin.site.register(PLC, PLCAdmin)
