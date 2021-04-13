# myapp
from django.db import models
from django.contrib.auth.models import User 

class Agency(models.Model):
    system_name = models.CharField(max_length=255)
    county = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    active = models.BooleanField(default=True)

    system_type_tuple = [('ED', 'School'),('PG','Power Generation'),('TF','Some other Facility'),('UN','Unknown')]
    system_type = models.CharField(max_length=2, choices=system_type_tuple, default= 'UN')
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=60, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    system_no = models.CharField(max_length=7, unique=True)
    
    def __str__(self):
        return self.system_no
    
class SitePart(models.Model):
    # I tried changing the "system_no" to another name "agency_no" through out the *.py's this did not resolve the problem
    # the db_column seems to matchup better than the to_field which enters and additional "_id" to the field name. 
    # system_no = models.ForeignKey('Agency', on_delete=models.CASCADE, db_column='system_no', null=False, blank=False, default=1)
    system_no = models.ForeignKey('Agency', on_delete=models.CASCADE, db_column='system_no', null=True, blank=True)
    # part name is only unique for the system number other systems will have the same of simular name
    part_name = models.CharField(max_length=125) 
    status_tuple = [('AB','Abandoned'),('AC','Active Compliant'),('DS','Destroyed'),('IA','Inactive'),
            ('SB','Stand By waiting acitvation'),('MO','Monitoring')]
    status = models.CharField(max_length=2, choices=status_tuple, default= 'SB')
    # sys_site_n system site number is ID that uses the system number plus additional numbers that is specific for the part_name
    sys_site_n = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.part_name

class County(models.Model):
    coid = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name