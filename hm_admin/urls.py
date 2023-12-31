from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns

urlpatterns = []

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
    # path('admin/', admin.site.urls),
    path('', include('orgs.urls')),
    path('auth/', include('custom_auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.headers = "هامة المدن"
admin.site.site_header = "هامة المدن"
admin.site.site_title = "هامة المدن"
admin.site.index_title = "هامة المدن"
admin.site.name = "هامة المدن"
admin.site.su = "هامة المدن"
