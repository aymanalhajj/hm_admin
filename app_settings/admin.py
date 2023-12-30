from django.contrib import admin
from .models import *

@admin.register(ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = ("id","name","section_manager")
    list_filter = ("id","name","section_manager")
    search_fields = ("name",)


@admin.register(ServiceSectionEmployee)
class ServiceSectionEmployeeAdmin(admin.ModelAdmin):
    list_display = ("id","service_section","service_type","employee")
    list_filter = ("service_section","service_type","employee")
    search_fields = ("name","service_type","service_section","employee")


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("id","name")
    search_fields = ("name",)

@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("id","name")
    search_fields = ("name",)

@admin.register(EmployeeRole)
class EmployeeRoleAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("id","name")
    search_fields = ("name",)

@admin.register(OrganizationType)
class OrganizationTypeAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("id","name")
    search_fields = ("name",)

@admin.register(OrderStage)
class OrderStageAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("id","name")
    search_fields = ("name",)

@admin.register(VisitStatus)
class VisitStatusAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("id","name")
    search_fields = ("name",)

@admin.register(ProjectSetting)
class ProjectSettingAdmin(admin.ModelAdmin):
    list_display = ("id","days_before_contract")
    list_filter = ("id","days_before_contract")
    search_fields = ("days_before_contract",)
