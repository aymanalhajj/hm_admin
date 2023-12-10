from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orgs.urls')),
    path('auth/', include('custom_auth.urls')),
]
