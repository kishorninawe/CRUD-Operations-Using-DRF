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
from django.urls import path, include

from modelviewset import views
from rest_framework.routers import DefaultRouter

"""
Using Routers
"""
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('employee', views.EmployeeViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

"""
Declaring path manually as:
    urlpatterns = [
        path('employee_list/', views.EmployeeViewSet.as_view({'get': 'list'}), name='employee_list'),
        path('employee_create/', views.EmployeeViewSet.as_view({'get': 'list', 'post': 'create'}), name='employee_create'),
        path('employee_update/id/<int:pk>', views.EmployeeViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='employee_update'),
        path('employee_delete/id/<int:pk>', views.EmployeeViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='employee_delete'),
        path('employee_details/id/<int:pk>', views.EmployeeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='employee_update'),
    ]
"""
