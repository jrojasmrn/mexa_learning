"""mexaeducation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
#Import settings for the media file only if debug = True
from django.conf import settings

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),
    # URLs from App Core
    path('', include('core.urls')),
    # URLs from App User_Profile
    path('profile/', include('user_profile.urls')),
    # URLs from App Courses
    path('courses/', include('courses.urls')),
    # URLs from App Social
    path('social/', include('social.urls')),
    #URLs from App Dashboard
    path('dashboard/', include('dashboard.urls'))
]

#Comprobar si el Debug está en marcha o desactivado
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)