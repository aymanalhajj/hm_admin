from django.contrib.admin.apps import AdminConfig


class CustomAdminConfig(AdminConfig):
    default_site = "hm_admin.admin.CustomAdminSite"


from django.contrib import admin

# admin.site.headers = "هامة المدن"
# admin.site.su = "هامة المدن"
# admin.site.site_header = "هامة المدن"
# admin.site.site_title = "هامة المدن"
# admin.site.index_title = "هامة المدن"
# admin.site.name = "هامة المدن"
