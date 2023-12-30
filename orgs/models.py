from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from custom_auth.models import UserAccount


YES_NO = (
    (0,_('no')),
    (1,_('yes'))
)

VISIT_STATE = (
    (1,_('agreed')),
    (2,_('disagreed'))
)


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
    
class ServiceType(models.Model):
    name = models.CharField(max_length= 100 ,null = False ,verbose_name=_("name") )
    def __str__(self) -> str:
        return self.name
    class Meta:
        managed = True
        verbose_name = _('Service Type')
        verbose_name_plural = _('Service Type')
    
class ServiceSection(models.Model):
    name = models.CharField(max_length= 100 ,null = False ,verbose_name=_("name") )
    section_manager =  models.ForeignKey(UserAccount,on_delete=models.DO_NOTHING,verbose_name=_("section manager") ,related_name="section_manager" , default= None, null= True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        managed = True
        verbose_name = _('Service Section')
        verbose_name_plural = _('Service Section')

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

class OrderStage(models.Model):
    name = models.CharField(max_length= 100 ,null = False ,verbose_name=_("name") )
    def __str__(self) -> str:
        return self.name
    class Meta:
        managed = True
        verbose_name = _('Order Stage')
        verbose_name_plural = _('Order Stages')


def file_location(instance, filename):
    file_path = f"images/{filename}"
    print(instance.id)
    return file_path
from django.utils import timezone

class Organization(models.Model):
    name = models.CharField(max_length= 100 ,null = False ,verbose_name=_("name") )
    org_type =  models.ForeignKey(OrganizationType,on_delete=models.DO_NOTHING,verbose_name=_("organization type") )
    order_status =  models.ForeignKey(OrderStatus,on_delete=models.DO_NOTHING,verbose_name=_("order status") )
    employee =  models.ForeignKey(UserAccount,on_delete=models.DO_NOTHING,verbose_name=_("employee") ,related_name="org_employee" , default= None, null= True)
    note = models.TextField(max_length=1000, null=True, verbose_name=_("note") )
    expected_date = models.DateField(null= True,verbose_name=_("expected date") )
    order_stage =  models.ForeignKey(OrderStage,on_delete=models.DO_NOTHING,verbose_name=_("order stage"),related_name="ord_stage", default= None, null= True,blank=True)#, default = OrderStage.objects.first().pk )
    image_url = models.ImageField(upload_to=file_location, blank=True, null=True)
    created_date = models.DateField(null= True,verbose_name=_("created date"),default=  timezone.now)
    # engineer =  models.ForeignKey(UserAccount,on_delete=models.DO_NOTHING,verbose_name=_("engineer") ,related_name="org_engineer", default= None, null= True)
    # manager =  models.ForeignKey(UserAccount,on_delete=models.DO_NOTHING,verbose_name=_("manager") ,related_name="org_manager", default= None, null= True)
    # admin_note = models.TextField(max_length=1000, null=True,verbose_name=_("admin note") ,blank=True)
    # engineer_note = models.TextField(max_length=1000, null=True,verbose_name=_("engineer note") )


    @property
    def org_employees(self):
        employees = ''
        employees += '<table class="myTable"> <thead> <tr><td>الإسم</td><td>الصفة</td><td>الجوال</td></tr></thead><tbody> '
        for c in self.organizationemployee_set.all():
            employees += f'<tr><td>{c.name}</td><td>{c.role}</td><td>{c.mobile}</td> </tr>'
        employees += '</tbody></table>'
        return format_html(employees) 
    org_employees.fget.short_description = _('organization employees')    
    @property
    def org_services(self):
        services = ''
        services += '<table class="myTable"> <thead> <tr><td>القسم</td><td>الخدمة</td></tr></thead><tbody> '
        for c in self.organizationservice_set.all():
            services += f'<tr><td>{c.service_section}</td><td>{c.service_type}</td></tr>'
        services += '</tbody></table>'
        return format_html(services) 
    org_services.fget.short_description = _('organization services')

    def __str__(self) -> str:
        return self.name
    class Meta:
        managed = True
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')


class OrganizationVisit(models.Model):
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,verbose_name=_("organization") )
    service_section = models.ForeignKey(ServiceSection,on_delete=models.CASCADE,verbose_name=_("service section") )
    service_type = models.ForeignKey(ServiceType,on_delete=models.CASCADE,verbose_name=_("service type") )
    visit_state = models.IntegerField(default=0,choices=VISIT_STATE ,verbose_name=_("visit state") )
    visit_note =  models.CharField(max_length= 100 ,null = False, blank=True ,verbose_name=_("visit note") )
    visitor = models.ForeignKey(UserAccount,on_delete=models.DO_NOTHING,verbose_name=_("visitor") ,related_name="org_visitor", default= None, null= True)
    is_reviewed = models.IntegerField(default=0,choices=YES_NO,verbose_name=_("is reviewed") )
    reviewer = models.ForeignKey(UserAccount,on_delete=models.DO_NOTHING,verbose_name=_("reviewer") ,related_name="org_reviewer", default= None, null= True)
    review_note =  models.CharField(max_length= 100 ,null = False, blank=True ,verbose_name=_("review note") )
    created_date = models.DateField(null= True,verbose_name=_("created date"),default=  timezone.now)
    class Meta:
        managed = True
        verbose_name = _('Organization Visit')
        verbose_name_plural = _('Organization Visits')

class OrganizationEmployee(models.Model):
    name = models.CharField(max_length= 100 ,null = False, blank=True ,verbose_name=_("name") )
    role =  models.ForeignKey(EmployeeRole,on_delete=models.DO_NOTHING,verbose_name=_("employee role") )
    mobile = models.CharField(max_length= 100 ,null = False , blank=True ,verbose_name=_("mobile number") )
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,verbose_name=_("organization") )
    def __str__(self) -> str:
        return self.name
    class Meta:
        managed = True
        verbose_name = _('Organization Employee')
        verbose_name_plural = _('Organization Employees')

class OrganizationService(models.Model):
    service_section = models.ForeignKey(ServiceSection,on_delete=models.CASCADE,verbose_name=_("service section") )
    service_type = models.ForeignKey(ServiceType,on_delete=models.CASCADE,verbose_name=_("service type") )
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,verbose_name=_("organization") )
    is_visited = models.IntegerField(default=0, verbose_name=_("is visited"))
    class Meta:
        managed = True
        verbose_name = _('Organization Service')
        verbose_name_plural = _('Organization Services')


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


