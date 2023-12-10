from django.db import models
from geo_location.models import GeoLocation


ORG_TYPE = (
    ('1','برج'),
    ('2','مركز تجاري')
)

ORDER_STATUS = (
    ('1','جديد'),
    ('2','تحديد تاريخ'),
    ('3','محتمل'),
)

EMPLOYEE_ROLE = (
    ('1','مالك'),
    ('2','موظف'),
    ('3','مدير'),
)

SERVICE_TYPE = (
    ('1','تركيب'),
    ('2','صيانة'),
    ('3','اعطال'),
)

SERVICE_SECTION = (
    ('1','امن'),
    ('2','مصاعد'),
)




class OrganizationType(models.Model):
    name = models.CharField(max_length= 100 ,null = False )
    def __str__(self) -> str:
        return self.name

class OrderStatus(models.Model):
    name = models.CharField(max_length= 100 ,null = False )
    def __str__(self) -> str:
        return self.name
    
class EmployeeRole(models.Model):
    name = models.CharField(max_length= 100 ,null = False )
    def __str__(self) -> str:
        return self.name
    
class ServiceType(models.Model):
    name = models.CharField(max_length= 100 ,null = False )
    def __str__(self) -> str:
        return self.name
    
class ServiceSection(models.Model):
    name = models.CharField(max_length= 100 ,null = False )
    def __str__(self) -> str:
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length= 100 ,null = False )
    org_type =  models.ForeignKey(OrganizationType,on_delete=models.DO_NOTHING)
    order_status =  models.ForeignKey(OrderStatus,on_delete=models.DO_NOTHING)
    note = models.CharField(max_length=1000, null=True)
    expected_date = models.DateField(null= True)
    # location = models.ForeignKey(GeoLocation, on_delete=models.SET_NULL, null=True, default= None)
    def __str__(self) -> str:
        return self.name

class OrganizationEmployee(models.Model):
    name = models.CharField(max_length= 100 ,null = False, blank=True )
    role =  models.ForeignKey(EmployeeRole,on_delete=models.DO_NOTHING)
    mobile = models.CharField(max_length= 100 ,null = False , blank=True )
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name

class OrganizationService(models.Model):
    service_section = models.ForeignKey(ServiceSection,on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType,on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)

