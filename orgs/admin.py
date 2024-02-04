from django.contrib import admin
from .models import *
# Register your models here.


from django.utils.html import format_html


@admin.register(OrganizationFile)
class OrganizationFileAdmin(admin.ModelAdmin):
    list_display = ('id','organization','file',"description",'created_by','created_at')
    list_filter = ('id','organization','description','created_by','created_at')
    search_fields = ("organization","description")

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name","org_type","order_status","employee","expected_date","org_employees","org_services")
    list_filter = ("employee","expected_date","org_type","order_status","note","order_stage")
    search_fields = ("id","name","org_type","order_status","note","expected_date")
    readonly_fields = ("created_date",)
    # exclude = ("image_url",)

    def services(self, obj: Organization) -> str:
        service_type = ''
        for c in obj.organizationservice_set.all():
            service_type += f'<div>القسم: {c.service_section}</div><div>الخدمة: {c.service_type}</div>'
        return format_html(service_type)
        # return format_html(f'<div>{self.organizationservice_set.service_section}</div>')


@admin.register(OrganizationVisit)
class OrganizationVisitAdmin(admin.ModelAdmin):
    list_display = ('id','organization','service_section','service_type','visit_state','visit_note','visitor','is_reviewed','review_note','reviewer',)
    list_filter = ('id','is_reviewed','service_type','service_section','visit_state','visit_note','organization','visitor',)
    search_fields = ("organization",)
    readonly_fields = ('organization','service_section','service_type','visit_state','visit_note','visitor','is_reviewed','review_note','reviewer','created_date')

@admin.register(VisitTask)
class VisitTaskAdmin(admin.ModelAdmin):
    list_display = ('id','organization','visitor','started_at','finished_at','task_state',)
    list_filter =  ('id','organization','visitor','started_at','finished_at','note','task_state',)
    search_fields = ("organization","visitor")
    execlude = ("note",)

@admin.register(OrganizationService)
class OrganizationServiceAdmin(admin.ModelAdmin):
    list_display = ("id","organization","service_section","service_type",'created_by')
    list_filter = ("id","service_section","service_type","organization")
    search_fields = ("id","service_section","service_type","organization")
    readonly_fields =  ("created_date",)
    def get_row_css(self, obj, index):
        print("obj.service_section"+obj.service_section)
        if obj.service_section==1:
            print("obj.service_section"+obj.service_section)
            return 'red red%d' % index
        return ''
    #,"is_visited")


@admin.register(OrganizationEmployee)
class OrganizationEmployeeAdmin(admin.ModelAdmin):
    list_display = ("id","organization","name","role","mobile",'created_by')
    list_filter = ("id","name","role","mobile","organization")
    search_fields = ("id","name","role","mobile","organization")
    readonly_fields =  ("created_date",)


# @admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id","name","org_type","order_status","note","expected_date")
    list_filter = ("id","name","org_type","order_status","note","expected_date")
    search_fields = ("id","name","org_type","order_status","note","expected_date")



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
