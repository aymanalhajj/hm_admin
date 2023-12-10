from django.contrib import admin
from .models import *
# Register your models here.


class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("id","name")
    search_fields = ("name",)

class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("id","name")
    search_fields = ("name",)

class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("id","name")
    search_fields = ("name",)

class EmployeeRoleAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("id","name")
    search_fields = ("name",)

class OrganizationTypeAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("id","name")
    search_fields = ("name",)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id","name","org_type","order_status","note","expected_date")
    list_filter = ("id","name","org_type","order_status","note","expected_date")
    search_fields = ("id","name","org_type","order_status","note","expected_date")


class OrganizationServiceAdmin(admin.ModelAdmin):
    list_display = ("id","service_section","service_type","organization")
    list_filter = ("id","service_section","service_type","organization")
    search_fields = ("id","service_section","service_type","organization")


class OrganizationEmployeeAdmin(admin.ModelAdmin):
    list_display = ("id","name","role","mobile","organization")
    list_filter = ("id","name","role","mobile","organization")
    search_fields = ("id","name","role","mobile","organization")


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id","name","org_type","order_status","note","expected_date")
    list_filter = ("id","name","org_type","order_status","note","expected_date")
    search_fields = ("id","name","org_type","order_status","note","expected_date")



# admin.site.register(Organization)

def _register(model, admin_class = None):
    admin.site.register(model,admin_class)

_register(OrganizationEmployee,OrganizationEmployeeAdmin)
_register(OrganizationService,OrganizationServiceAdmin)
_register(Organization,OrganizationAdmin)
_register(ServiceSection,ServiceSectionAdmin)
_register(ServiceType,ServiceTypeAdmin)
_register(OrderStatus,OrderStatusAdmin)
_register(EmployeeRole,EmployeeRoleAdmin)
_register(OrganizationType,OrganizationTypeAdmin)
