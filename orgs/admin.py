from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(OrganizationVisit)
class OrganizationVisitAdmin(admin.ModelAdmin):
    list_display = ('id','organization','service_section','service_type','visit_state','visit_note','visitor','is_reviewed','review_note','reviewer',)
    list_filter = ('id','is_reviewed','service_type','service_section','visit_state','visit_note','organization','visitor',)
    search_fields = ("organization",)


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


# @admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id","name","org_type","order_status","note","expected_date")
    list_filter = ("id","name","org_type","order_status","note","expected_date")
    search_fields = ("id","name","org_type","order_status","note","expected_date")


@admin.register(OrganizationService)
class OrganizationServiceAdmin(admin.ModelAdmin):
    list_display = ("id","service_section","service_type","organization")
    list_filter = ("id","service_section","service_type","organization")
    search_fields = ("id","service_section","service_type","organization")


@admin.register(OrganizationEmployee)
class OrganizationEmployeeAdmin(admin.ModelAdmin):
    list_display = ("id","name","role","mobile","organization")
    list_filter = ("id","name","role","mobile","organization")
    search_fields = ("id","name","role","mobile","organization")


from django.utils.html import format_html

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name","org_type","order_status","note","expected_date","org_employees","org_services")
    list_filter = ("employee","expected_date","org_type","order_status","note",)
    search_fields = ("id","name","org_type","order_status","note","expected_date")
    readonly_fields = ("name","org_type","order_status","employee","note","order_stage","expected_date","created_date")
    exclude = ("image_url",)

    def services(self, obj: Organization) -> str:
        service_type = ''
        for c in obj.organizationservice_set.all():
            service_type += f'<div>القسم: {c.service_section}</div><div>الخدمة: {c.service_type}</div>'
        return format_html(service_type)
        # return format_html(f'<div>{self.organizationservice_set.service_section}</div>')

# admin.site.register(Organization)

def _register(model, admin_class = None):
    admin.site.register(model,admin_class)



# # _register(ServiceSectionEmployee,ServiceSectionEmployeeAdmin)
# _register(OrganizationEmployee,OrganizationEmployeeAdmin)
# _register(OrganizationService,OrganizationServiceAdmin)
# _register(Organization,OrganizationAdmin)
# _register(ServiceSection,ServiceSectionAdmin)
# _register(ServiceType,ServiceTypeAdmin)
# _register(OrderStatus,OrderStatusAdmin)
# _register(EmployeeRole,EmployeeRoleAdmin)
# _register(OrganizationType,OrganizationTypeAdmin)
# _register(OrderStage,OrderStageAdmin)
