# core/admin.py

from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.urls import path


@staff_member_required
def admin_statistics_view(request):
    return render(request, "admin/statistics.html", {
        "title": "مؤشرات الأداء"
    })


class CustomAdminSite(admin.AdminSite):
    def get_app_list(self, request, _=None):
        app_list = super().get_app_list(request)
        app_list += [
            {
                "name": "تحليل البيانات",
                "app_label": "my_custom_app",
                "models": [
                    {
                        "name": "مؤشرات الأداء",
                        "object_name": "مؤشرات الأداء",
                        "admin_url": "/admin/statistics",
                        "view_only": True,
                    },
                    {
                        "name": "خارطة الإنتشار",
                        "object_name": "خارطة الإنتشار",
                        "admin_url": "/admin/get-clients-map",
                        "view_only": True,
                    }
                ],
            }
        ]
        return app_list

    def get_urls(self):
        urls = super().get_urls()
        # urls += [
        #     path("statistics/", admin_statistics_view, name="admin-statistics"),
        # ]
        return urls
# from orgs.models import Organization
# admin_site = CustomAdminSite(name="myadmin")
# # admin.site.register(Organization)

# admin.site.headers = "هامة المدن"
# admin.site.su = "هامة المدن"
# admin.site.site_header = "هامة المدن"
# admin.site.site_title = "هامة المدن"
# admin.site.index_title = "هامة المدن"
# admin.site.name = "هامة المدن"
