from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import EmployeeDetail
from employee.models import EmployeeDetail
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView


# Create your views here.
class ViewAllEmployee(ListView):
	model=EmployeeDetail
	template_name="view_all_data.html"

class ViewEmployeeDetail(DetailView):
	model=EmployeeDetail
	template_name='view_one_data.html'
class CreateEmployeeDetail(CreateView):
	model=EmployeeDetail
	fields = "__all__"
	template_name='create_employee.html'



def index(request):
	return HttpResponse('Hi')

def ViewEmployee(request):
	view_employee_obj = EmployeeDetail.objects.all()
	print(view_employee_obj.query)
	#render(request,template name,dict objects)
	return render(request,'view_employee.html',{'view_employee_obj':view_employee_obj})

def add_employee(request):
	return render(request,'insert_employee.html')

def emp_portal(request):
	emp_name = request.POST.get('name')
	emp_salary = request.POST.get('salary')
	emp_desgination = request.POST.get('desgination')
	emp_city = request.POST.get('city')
	print(emp_name,':',emp_salary,':',emp_desgination,':',emp_salary)
	e1 = EmployeeDetail()
	e1.emp_name = emp_name
	e1.emp_salary = emp_salary
	e1.emp_desgination = emp_desgination
	e1.emp_city = emp_city
	e1.save()
	id=EmployeeDetail.objects.latest('emp_id')
	print(id)
	return render(request,'registeremployee.html',{'emp_id':id})








	



