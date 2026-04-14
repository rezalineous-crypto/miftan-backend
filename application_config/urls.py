from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = [
    path('api/auth/', include('auth_management_system.urls')),   
    path('api/com/', include('com_management_system.urls')),
    path('api/mgn/', include('migration_management_system.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
