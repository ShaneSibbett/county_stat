from import_export import fields, resources, widgets
from import_export.widgets import ForeignKeyWidget
from myapp.models import Agency, SitePart
 
class AgencyResource(resources.ModelResource):
    class Meta:
        model = Agency
        import_id_fields = ('system_no',)
        fields = ('system_name', 'county', 'state', 'active', 
            'system_type', 'address', 'city', 'zipcode','system_no',)
        

class SitePartResource(resources.ModelResource):
    class SysNumForeignKeyWidget(ForeignKeyWidget):
        def get_queryset(self, value, row):
            print(int(value), row)
            qs= SysNum.objects.filter(
                id=str(value),)
            print("returning:", qs)
            return qs

    system_no = fields.Field(
        column_name='system_no',
        attribute='system_no',
        widget=ForeignKeyWidget(Agency,'system_no'))
        # column_name='agency_no', -- this did't work. 
        # attribute='agency_no',

    class Meta:
        model = SitePart
        raise_errors = True
        import_id_fields = ('system_no',)
        fields = ('system_no','part_name','status', 'sys_site_n',)

    
    # def dehydrate_system_no(self, site):
    #     return site.system_no.system_no #-- this didn't work.