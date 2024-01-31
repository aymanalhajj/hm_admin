from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin
from django.urls import path, include

from orgs import site_views
from .admin import admin_statistics_view  # new
# from .admin import admin_site

urlpatterns = []

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
    # path('admin/', admin.site.urls),
    path('', include('orgs.urls')),
    path('auth/', include('custom_auth.urls')),
    path("admin/statistics/", admin.site.admin_view(admin_statistics_view),name="admin-statistics"),
    # path("myadmin/", admin_site.urls),
    path("admin/get-clients-map/", admin.site.admin_view(site_views.get_clients_map),name="admin-statistics"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.headers = "هامة المدن"
admin.site.site_header = "هامة المدن"
admin.site.site_title = "هامة المدن"
admin.site.index_title = "هامة المدن"
admin.site.name = "هامة المدن"
admin.site.su = "هامة المدن"
