"""qrs URL Configuration

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
from django.urls import path,include
from employee import views
from employee.views import ViewAllEmployee
from employee.views import ViewEmployeeDetail,CreateEmployeeDetail

urlpatterns = [
	path('',views.index,name='index'),
	path('view_employee/',views.ViewEmployee,name='view_employee'),
	path('insert_employee/',views.add_employee,name='insert_employee'),
	path('reg_employee/',views.emp_portal,name='reg_employee'),
    path('view_all_data/',ViewAllEmployee.as_view(),name='view_all_data'),
    path('view_one_data/<int:pk>',ViewEmployeeDetail.as_view(),name='view_one_data'),
    path('create_employee/', CreateEmployeeDetail.as_view(),name='create_employee'),

]


