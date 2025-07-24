"""
URL configuration for Food5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin    # Import admin to manage the Django admin interface
from django.urls import path, include   # Import include to include other URL configurations
from django.conf import settings  
from django.conf.urls.static import static  # Import static to serve media files during development
from Food5_app.views import exportAllToCsv  # Import the view for exporting data to CSV

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Food5 API",
        default_version='v1',
        description="Documentación de la API del proyecto Food5",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/', include('app_drink.urls')),
    path('bread/', include('app_Bread.urls')),
    path('first_course/', include('app_first_course.urls')),
    path('second_course/', include('app_second_course.urls')),
    path('dessert/', include('app_dessert.urls')),
    path('customer/', include('app_customer.urls')),
    path('menu/', include('app_menu.urls')),
    path('order/', include('app_order.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('export/csv/', exportAllToCsv, name='export_csv'),  # URL for exporting all data to CSV

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


""" When DEBUG = False (in production), Django does not serve media files. This is because:path('customer/', include('app_customer.urls'))
Django’s built-in server is not designed to efficiently or securely serve static/media files in production.
In production, you should use a proper web server (like Nginx or Apache) to serve files from MEDIA_ROOT.
 """

if settings.DEBUG:# allows Django to serve uploaded images during development.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)