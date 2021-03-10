from import_export import fields, resources, widgets
from import_export.widgets import ForeignKeyWidget
from myapp.models import Agency, SitePart
 
class AgencyResource(resources.ModelResource):
    class Meta:
        model = Agency
        fields = ('system_name', 'county', 'state', 'active', 
            'system_type', 'address', 'city', 'zipcode','system_no' )
        import_id_fields = ('system_no',)

class SitePartResource(resources.ModelResource):
    # class SystemNoForeignKeyWidget(widgets.ForeignKeyWidget):
    #     def get_queryset(self, value, row):
    #         return self.model.objects.filter(systen_no__iexact=row['system_no'],)

    system_no = fields.Field(
        column_name='system_no',
        attribute='system_no',
        widget=ForeignKeyWidget(Agency,'system_no'))

    class Meta:
        
        # import_id_fields = ('sys_site_n',)
        fields = ('system_no','part_name','status', 'sys_site_n',)
        import_id_fields = ['sys_site_n']
        model = SitePart