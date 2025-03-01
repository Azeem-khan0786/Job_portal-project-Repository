"""
URL configuration for job_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from JobApp.views import job_view 


urlpatterns = [
    path('', job_view, name='job_view'),
    path('admin/', admin.site.urls),
    path('Account/',include('Account.urls')),
    path('JobApp/',include('JobApp.urls')),
    path('',include('jsonApp.urls')),
    path('__reload__/',include('django_browser_reload.urls')),

    
     # Redirect the root URL to the admin page
    
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
