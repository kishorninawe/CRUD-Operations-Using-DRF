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
from django.urls import path

from generics import views

urlpatterns = [
    path('employee_list/', views.EmployeeList.as_view(), name='employee_list'),
    path('employee_create/', views.EmployeeCreate.as_view(), name='employee_create'),
    path('employee_retrieve/id/<int:pk>', views.EmployeeRetrieve.as_view(), name='employee_retrieve'),
    path('employee_update/id/<int:pk>', views.EmployeeUpdate.as_view(), name='employee_update'),
    path('employee_delete/id/<int:pk>', views.EmployeeDelete.as_view(), name='employee_delete'),
    path('employee_details/id/<int:pk>', views.EmployeeDetails.as_view(), name='employee_details'),
]
