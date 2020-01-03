"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app import views
from apiview import urls as apiview_urls
from generics import urls as generics_urls
from modelviewset import urls as modelviewset_urls
from apiview_decorator import urls as apiview_decorator_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cbv/apiview/', include(apiview_urls)),
    path('cbv/generics/', include(generics_urls)),
    path('cbv/modelviewset/', include(modelviewset_urls)),
    path('fbv/apiview_decorator/', include(apiview_decorator_urls)),
]
