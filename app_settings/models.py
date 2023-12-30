from django.db import models
from django.utils.translation import gettext_lazy as _
from custom_auth.models import UserAccount

class OrganizationType(models.Model):
    name = models.CharField(max_length= 100 ,null = False,verbose_name=_("name") )
    def __str__(self) -> str:
        return self.name
    class Meta:
        managed = True
        verbose_name = _('Organization Type')
        verbose_name_plural = _('Organization Type')

class OrderStatus(models.Model):
    name = models.CharField(max_length= 100 ,null = False ,verbose_name=_("name") )
    def __str__(self) -> str:
        return self.name
    class Meta:
        managed = True
        verbose_name = _('Order Status')
        verbose_name_plural = _('Order Statuses')
    
class VisitStatus(models.Model):
    name = models.CharField(max_length= 100 ,null = False ,verbose_name=_("name") )
    def __str__(self) -> str:
        return self.name
    class Meta:
        managed = True
        verbose_name = _('Visit Status')
        verbose_name_plural = _('Visit Statuses')
    
class EmployeeRole(models.Model):
    name = models.CharField(max_length= 100 ,null = False ,verbose_name=_("name") )
    def __str__(self) -> str:
        return self.name
    class Meta:
        managed = True
        verbose_name = _('Employee Role')
        verbose_name_plural = _('Employee Role')

class OrderStage(models.Model):
    name = models.CharField(max_length= 100 ,null = False ,verbose_name=_("name") )
    def __str__(self) -> str:
        return self.name
    class Meta:
        managed = True
        verbose_name = _('Order Stage')
        verbose_name_plural = _('Order Stages')

class ServiceSection(models.Model):
    name = models.CharField(max_length= 100 ,null = False ,verbose_name=_("name") )
    section_manager =  models.ForeignKey(UserAccount,on_delete=models.SET_NULL,verbose_name=_("section manager") ,related_name="section_manager" , default= None, null= True,blank=True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        managed = True
        verbose_name = _('Service Section')
        verbose_name_plural = _('Service Section')
    
class ServiceType(models.Model):
    name = models.CharField(max_length= 100 ,null = False ,verbose_name=_("name") )
    def __str__(self) -> str:
        return self.name
    class Meta:
        managed = True
        verbose_name = _('Service Type')
        verbose_name_plural = _('Service Type')
    

class ServiceSectionEmployee(models.Model):
    service_section = models.ForeignKey(ServiceSection,on_delete=models.CASCADE,verbose_name=_("service section") , default= None, null= True)
    service_type = models.ForeignKey(ServiceType,on_delete=models.CASCADE,verbose_name=_("service type") , default= None, null= True)
    employee =  models.ForeignKey(UserAccount,on_delete=models.CASCADE,verbose_name=_("section engineer") , default= None, null= True)
    def __str__(self) -> str:
        return self.service_section.name
    class Meta:
        managed = True
        verbose_name = _('Service Section Employee')
        verbose_name_plural = _('Service Section Employees')


class ProjectSetting(models.Model):
    days_before_contract = models.IntegerField(null = False ,verbose_name=_("days before contract") )
    class Meta:
        managed = True
        verbose_name = _('Project Setting')
        verbose_name_plural = _('Project Settings')
