from django.db import models

from django.utils.translation import gettext_lazy as _

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
    def __str__(self) -> str:
        return self.name
    class Meta:
        managed = True
        verbose_name = _('Service Section')
        verbose_name_plural = _('Service Section')


from django.utils.html import format_html

class Organization(models.Model):
    name = models.CharField(max_length= 100 ,null = False ,verbose_name=_("name") )
    org_type =  models.ForeignKey(OrganizationType,on_delete=models.DO_NOTHING,verbose_name=_("organization type") )
    order_status =  models.ForeignKey(OrderStatus,on_delete=models.DO_NOTHING,verbose_name=_("order status") )
    note = models.CharField(max_length=1000, null=True,verbose_name=_("note") )
    expected_date = models.DateField(null= True,verbose_name=_("expected date") )
    @property
    def org_employees(self):
        employees = ''
        # employees = "<style> .myTable , .myTable th, .myTable td '{'border: 1px solid black;'}' .myTable { border-collapse: collapse; width: 100%;}"
        # employees += ".myTable th,.myTable td '{'padding: 8px;text-align: center;'}' .myTable tr:hover {background-color: #D6EEEE;}</style>"
        employees += '<table class="myTable"> <thead> <tr><td>الإسم</td><td>الصفة</td><td>الجوال</td></tr></thead><tbody> '
        for c in self.organizationemployee_set.all():
            employees += f'<tr><td>{c.name}</td><td>{c.role}</td><td>{c.mobile}</td> </tr>'
        employees += '</tbody></table>'
        return format_html(employees) 
    org_employees.fget.short_description = _('organization employees')

    
    @property
    def org_services(self):
        services = ''
        # employees = "<style> .myTable , .myTable th, .myTable td '{'border: 1px solid black;'}' .myTable { border-collapse: collapse; width: 100%;}"
        # employees += ".myTable th,.myTable td '{'padding: 8px;text-align: center;'}' .myTable tr:hover {background-color: #D6EEEE;}</style>"
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
    class Meta:
        managed = True
        verbose_name = _('Organization Service')
        verbose_name_plural = _('Organization Services')

