from django.urls import path,include

from . import views

urlpatterns= [
    path('create-organization', views.create_organization),
    path('create-org-emp', views.create_organization_emp),
    path('create-org-service', views.create_organization_service),
    path('get-organizations', views.get_organizations_all),
    path('get-org-emps', views.get_org_emps_all),
    path('get-org-services', views.get_org_service_all),
    path('get-org-types', views.get_org_types),
    path('get-order-status', views.get_order_status),
    path('get-emp-roles', views.get_emp_roles),
    path('get-service-types', views.get_service_types),
    path('get-service-sections', views.get_service_sections),
]