from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from myapp.resources import AgencyResource, SitePartResource
from myapp.models import (Agency, County, SitePart)
# I was missing SitePartResources above 
# and resource_class = AgencyResource below, not working yet
# @admin.register(Agency)
class AgencyAdmin(ImportExportModelAdmin):
    resource_class = AgencyResource
    list_display = ('system_name', 'county', 'state', 'active', 
        'system_type', 'address', 'city', 'zipcode', 'system_no',)

# @admin.register(SitePart)
class SitePartAdmin(ImportExportModelAdmin):
    list_display = ('system_no', 'part_name', 'status', 'sys_site_n',)
    search_fields = ['system_no',] # Tried removing this, didn't work
    raise_errors = True
    resource_class = SitePartResource
    

admin.site.register(Agency, AgencyAdmin)
admin.site.register(County)
admin.site.register(SitePart, SitePartAdmin)
