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
    def has_delete_permission(self, request, obj=None):
        return False

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
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(VisitStatus)
class VisitStatusAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("id","name")
    search_fields = ("name",)
    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("id","name")
    search_fields = ("name",)
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(ProjectSetting)
class ProjectSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if ProjectSetting.objects.all().count() > 0 :
            return ("add" in request.path or "change" in request.path)
        else :
            return ("add")
    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
    list_display = ("id","days_before_contract")
    list_filter = ("id","days_before_contract")
    search_fields = ("days_before_contract",)