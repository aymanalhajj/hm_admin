from django.urls import path,include,re_path

from . import views
from app_settings.views import get_org_types,get_order_status,get_emp_roles,get_service_types,get_service_sections,get_order_stages
from app_settings.views import get_visit_status
from . import site_views
urlpatterns= [
    
    path('create-organization', views.create_organization_with_location),
    path('update-organization-location', views.update_organization_location),
    path('create-org-emp', views.create_organization_emp),
    path('create-org-service', views.create_organization_service),

    path('visit-organization', views.visit_organization),
    path('review-organization-visit', views.review_organization_visit),
    path('submit-organization-for-study', views.submit_organization_for_study),

    path('start-org-visit-task', views.start_organization_visit_task),
    path('finish-org-visit-task', views.finish_organization_visit_task),
    path('get-new-visit-tasks', views.get_new_visit_tasks),
    path('get-in-progress-visit-tasks', views.get_in_progress_visit_tasks),

    path('get-clients-map', site_views.get_clients_map),

    
    path('remove-org-file', views.remove_organization_file),
    path('upload-org-file', views.upload_organization_file),

    path('upload-org-image', views.upload_organization_image),
    path('download-org-image', views.download_organization_image),

    path('get-organizations', views.get_organizations_all),
    path('get-organization-list', views.get_organization_list),
    path('get-organization', views.get_organization),
    path('get-organizations-for-visit', views.get_organizations_for_visit),
    path('get-organizations-for-review', views.get_organizations_for_review),
    
    # path('update-org-note', views.update_organization_by_engineer),
    # path('get-org-emps', views.get_org_emps_all),
    # path('get-org-services', views.get_org_service_all),

    path('get-order-stages', get_order_stages),
    path('get-org-types', get_org_types),
    path('get-order-status', get_order_status),
    path('get-visit-status', get_visit_status),
    path('get-emp-roles', get_emp_roles),
    path('get-service-types', get_service_types),
    path('get-service-sections', get_service_sections),
    # path('get-organizations-by-state', site_views.get_organizations_by_state),
    # path('get-organizations-by-emp', site_views.get_organizations_by_emp),
    # path('get-organizations-by-section', site_views.get_organizations_by_section),
    # path('get-organization-visit-by-emp', site_views.get_organization_visit_by_emp),
    # re_path(r'^get-organization-for-visit-by-section/<str:from_date>',site_views.get_organization_for_visit_by_section),
    re_path(r'^get-organizations-by-state/(?P<from_date>\w+)?(/(?P<to_date>\w+)/?)?$', site_views.get_organizations_by_state),
    re_path(r'^get-organizations-by-emp/(?P<from_date>\w+)?(/(?P<to_date>\w+)/?)?$', site_views.get_organizations_by_emp),
    re_path(r'^get-organizations-by-section/(?P<from_date>\w+)?(/(?P<to_date>\w+)/?)?$', site_views.get_organizations_by_section),
    re_path(r'^get-organization-visit-by-emp/(?P<from_date>\w+)?(/(?P<to_date>\w+)/?)?$', site_views.get_organization_visit_by_emp),
    re_path(r'^get-organization-for-visit-by-section/(?P<from_date>\w+)?(/(?P<to_date>\w+)/?)?$',site_views.get_organization_for_visit_by_section)
    # path("statistics/", site_views.statistics_view, name="shop-statistics"),  # new

]