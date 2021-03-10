from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from myapp.resources import SitePartResource
from myapp.models import (Agency, County, SitePart)

# Register your models here.
@admin.register(Agency)
class AgencyAdmin(ImportExportModelAdmin):
    list_display = ('system_name', 'county', 'state', 'active', 'system_type', 'address', 'city', 'zipcode', 'system_no',)


admin.site.register(County)

@admin.register(SitePart)
class SitePartAdmin(ImportExportModelAdmin):
    list_display = ('system_no', 'part_name', 'status', 'sys_site_n',)
    search_fields = ['system_no',]
    # inlines = [DetailsInlineAdmin]
    resource_class = SitePartResource
    
# admin.site.register(SitePart, SitePartAdmin) 
    # pass
# admin.site.register(SystemNumber)
