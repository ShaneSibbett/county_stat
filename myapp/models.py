# myapp
from django.db import models
from django.contrib.auth.models import User 


class Agency(models.Model):
    system_name = models.CharField(max_length=255)
    county = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    active = models.BooleanField(default=True)


    system_type_tuple = [('C', 'Community'),('NC','Non-Community'),('NP','Irrigation'),('TC','Temporary Community'),('UN','Unknown')]
    system_type = models.CharField(max_length=2, choices=system_type_tuple, default= 'UN')
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=60, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    system_no = models.CharField(max_length=7, unique=True)
    # class Meta:
    #     unique_together = ('system_name', 'system_no',)
    
    def __str__(self):
        return self.system_no
    


class County(models.Model):
    coid = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class SitePart(models.Model):
    system_no = models.ForeignKey('Agency', on_delete=models.CASCADE, to_field='system_no', null=True, blank=True)
    # part name is only unique for the system number other systems will have the same of simular name
    part_name = models.CharField(max_length=125) 
    status_tuple = [('AB','Abandoned'),('DS','Destroyed'),('IA','Inactive'),('AR','Active Recorder'),('AT','Active Treatment Facility'),('SB','Stand By waiting acitvation'),('MO','Monitoring')]
    status = models.CharField(max_length=2, choices=status_tuple, default= 'SB')
    # sys_site_n system site number is ID that uses the system number plus additional numbers that is specific for the part_name
    sys_site_n = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.part_name