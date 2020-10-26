from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import Products
from .models import CustomerDetail
from .models import CategoryView
# from .models import OrderMasterPage
from .models import OrderDetail
from django.conf import settings
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
import csv
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CustomerForm
from jabong.models import CustomerDetail
from .forms import ProductForm,OrderForm
from django.urls import reverse_lazy
from .forms import RegisterpageForm
from reportlab.pdfgen import canvas  
import io
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
 










# Create your views here.


# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:list')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})
 
 
# def login_view2(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             return redirect('posts:list')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login_user.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'user_login.html', {'form': form})


class user_login(LoginView):
	template_name = 'user_login.html'
@login_required
def home(request):
    return render(request, 'user_home.html')
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(request, username=email, password=password)
                login(request, user)
                return HttpResponseRedirect('/')    
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
                
    else:
        form = UserRegistrationForm()

        
    return render(request, 'user_register.html', {'form' : form})


def thanks(request):
    return HttpResponse("Thank you! Will get in touch soon.")
def customer_create_form(request):
	if request.method =='POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('customer_create_form')
	else:
		form = CustomerForm()
		return render(request,'customer_create.html',{'form':form})

def customer_edit(request,pk=None):
	edit = get_object_or_404(CustomerDetail,pk=pk)
	if request.method == "POST":
		form = CustomerForm(request.POST,instance=edit)
		if form.is_valid():
			form.save()
			return redirect('customer_create_form')
	else:
		form= CustomerForm(instance=edit)

	return render(request,'customer_edit.html',{'form':form,'edit':edit})
def customer_delete(request,pk=None):
	delete = get_object_or_404(CustomerDetail, pk=pk)
	if request.method == "POST":
		form = CustomerForm(request.POST,instance=delete)
		if form.is_valid():
			delete.delete()
			return redirect('customer_create_form')

	else:
		form = CustomerForm(instance=delete)
		
	return render(request,'customer_delete.html',{'form':form,'delete':delete})		

def product_create_form(request):
	if request.method =='POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('view_products')
	else:
		form = ProductForm()
		return render(request,'insert_product.html',{'form':form})
def edit_product(request,pk=None):
	edit = get_object_or_404(Products,pk=pk)
	if request.method == "POST":
		form = ProductForm(request.POST,instance=edit)
		if form.is_valid():
			form.save()
			return redirect('product_create_form')
	else:
		form= ProductForm(instance=edit)

	return render(request,'product_edit.html',{'form':form,'edit':edit})

def product_delete(request,pk=None):
	delete = get_object_or_404(Products, pk=pk)
	if request.method == "POST":
		form = ProductForm(request.POST,instance=delete)
		if form.is_valid():
			delete.delete()
			return redirect('product_create_form')

	else:
		form = ProductForm(instance=delete)
		
	return render(request,'delete_product.html',{'form':form,'delete':delete})

def order_form(request):
	if request.method =='POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('order_form')
	else:
		form = OrderForm()
		return render(request,'placeorder.html',{'form':form})

def edit_order(request,pk=None):
	edit = get_object_or_404(OrderDetail,fk=product_id)
	if request.method == "POST":
		form = OrderForm(request.POST,instance=edit)
		if form.is_valid():
			form.save()
			return redirect('order_form')
	else:
		form= OrderForm(instance=edit)

	return render(request,'order_edit.html',{'form':form,'edit':edit})

def order_delete(request,pk=None):
	delete = get_object_or_404(OrderDetail, fk=fk)
	if request.method == "POST":
		form = OrderForm(request.POST,instance=delete)
		if form.is_valid():
			delete.delete()
			return redirect('order_form')

	else:
		form = OrderForm(instance=delete)
		
	return render(request,'delete_order.html',{'form':form,'delete':delete})

def index(request):
	return HttpResponse('Welcome')



class productdetail(DetailView):
	models=Products
	template_name="view_all_products.html"


class category_product(ListView):
	model=CategoryView
	template_name='category_view.html'

class create_one_category(CreateView):
	model=CategoryView
	fields = "__all__"
	template_name='create_category.html'



@login_required
def add_category(request):
	return render(request,'category_insert.html')


@login_required
def category_protal(request):
	category_name = request.POST.get('name')
	category_picture = request.POST.get('picture')
	category_description = request.POST.get('description')
	print(category_name,':',category_picture,':',category_description)
	m1=CategoryView()
	m1.category_name=category_name
	m1.category_picture=category_picture
	m1.category_description=category_description
	m1.save()
	id=Products.objects.latest('category_id')
	return render(request,'insertcategory.html',{'category_id':id})
	

class create_one_product(CreateView):
	model=Products
	fields = "__all__"
	template_name='create_product.html'

@login_required
def view_order(request):
	print('view Enter')
	pid=request.POST.get('prod')
	# odobj=OrderDetail.objects.all()
	

	cid=request.POST.get('cust')
	odate=request.POST.get('d_date')
	qty=request.POST.get('productquantity')
	print(pid)
	print(odate)
	print(qty)
	
	ord = OrderDetail()
	ord.product_id=Products.objects.get(product_id=pid)
	ord.customer_data_id=CustomerDetail.objects.get(customer_id=cid)
	ord.order_quantity=qty 
	ord.save()
	# print(k)
	x=OrderDetail.objects.latest('order_detail_id')
	# print(ord.order_detail_id)
	# pobj = Products.objects.all()
	# od =OrderDetail.objects.all()
	# return HttpResponse('order')
	# return render(request,'orderpage.html',{'pobj':pobj,'od':od})
	return render(request,'orderpage.html',{'order_detail_id' :x})
@login_required
def add_order(request):
	pobj=Products.objects.all()
	custobj=CustomerDetail.objects.all()
	# ordobj= OrderMasterPage.objects.all()
	# print(custobj)
	return render(request,'add_order.html',{'pobj':pobj,'custobj':custobj})

# def order_portal(request):
# 	order_quantity = request.POST.get('productquantity')
# 	print(order_quantity,':',product_quantity,':')

# 	o1=Products()
# 	o1.order_quantity = order_quantity
# 	o1.product_quantity =product_quantity
# 	o1.save()
# 	id=OrderDetail.objects.latest('order_detail_id')
# 	return render(request,'orderpage.html',{'order_detail_id':id})

# def login_page(request):
# 		custobj=CustomerDetail.objects.all()
# 		return render(request,'loginpage.html',{'custobj':custobj})


@login_required
def view_products(request):
	product_obj=Products.objects.all()
	return render(request,'view_all_product.html',{'products_all':product_obj} )
@login_required
def add_product(request):
	return render(request,'product_insert.html')

@login_required
def product_portal(request):
	product_name = request.POST.get('name')
	product_price = request.POST.get('price')
	product_image = request.POST.get('image')
	product_quantity = request.POST.get('productquantity')
	product_features = request.POST.get('productfeatures')
	print(product_name,':',product_price,':',product_image,':',product_quantity,':',product_features)

	n1=Products()
	n1.product_name = product_name
	n1.product_price = product_price
	n1.product_image = product_image
	n1.product_quantity =product_quantity
	n1.product_features = product_features
	n1.save()
	id=Products.objects.latest('product_id')
	return render(request,'orderpage.html',{'product_id':id})

class customer_insert(CreateView):
	model=CustomerDetail
	fields="__all__"
	template_name="create_customer.html"




class view_customer(ListView):
	model=CustomerDetail
	template_name="customer_view.html"
@login_required
def add_customer(request):
	return render(request,'customer_detail.html')



@login_required
def customer_portal(request):
	customer_name = request.POST.get('name')
	customer_email = request.POST.get('email')
	customer_address = request.POST.get('address')
	customer_phone = request.POST.get('phone')
	customer_city = request.POST.get('city')
	customer_pincode = request.POST.get('pincode')
	customer_landmark = request.POST.get('landmark')
	print(customer_name,':',customer_email,':',customer_address,':',customer_phone,':',customer_city,':',customer_pincode,':',customer_landmark)
	e1 = CustomerDetail()
	e1.customer_name = customer_name
	e1.customer_email = customer_email
	e1.customer_address = customer_address
	e1.customer_phone = customer_phone
	e1.customer_city = customer_city
	e1.customer_pincode = customer_pincode
	e1.customer_landmark = e1.customer_landmark
	e1.save()
	id=CustomerDetail.objects.latest('customer_id')
	return render(request,'registercustomer.html',{'customer_id':id})


class order_detail_page(ListView):
		model=CustomerDetail
		template_name='order_detail_page.html'


@login_required
def view_one_order(request):

	return render(request,'one_order_id.html')
@login_required
def get_one_order(request):
	print('orderid')
	cust = request.POST.get('cust_id')
	print('cust Id  : ', cust)
	# pobj=Products.objects.get(product_id=)
	# custobj = CustomerDetail.objects.get(product_id=cust)
	ordobj=OrderDetail.objects.filter(customer_data_id=cust)
	print(ordobj,' nos ',len(ordobj))
	return render(request,'getorder.html',{'ordobj':ordobj})


@login_required	
def category_view(request):
	print('category')
	cateobj = CategoryView.objects.all()
	return render(request,'category_product_view.html',{'cateobj':cateobj})

@login_required
def product_category_view(request):
	print('hi')
	cate =request.POST.get('categoryname')
	print('category id  : ', cate)
	
	prodobj = Products.objects.filter(category_view_id=cate)
	return render(request,'product_view.html',{'prodobj':prodobj})



@login_required
def order_page(request,order_prod):
	print(order_prod)
	return render(request,'order_product.html',{'order_prod':order_prod})


@login_required		
def order_placed(request):
	print('hi')
	pid=request.POST.get('product_id')
	cid=request.POST.get('customer_id')
	qty=request.POST.get('productquantity')
	print(cid)
	print(qty)
	print(pid)
	
	ord = OrderDetail()
	ord.product_id=Products.objects.get(product_id=pid)
	ord.customer_data_id=CustomerDetail.objects.get(customer_id=cid)
	ord.order_quantity=qty 
	ord.save()
	# print(k)
	id=OrderDetail.objects.latest('order_detail_id')
	# print(ord.order_detail_id)
	# pobj = Products.objects.all()
	# od =OrderDetail.objects.all()
	# return HttpResponse('order')
	# return render(request,'orderpage.html',{'pobj':pobj,'od':od})
	return render(request,'orderpage.html',{'order_detail_id' :id})

def user_loginpage(request):
	return render(request,'user_login_page.html')
def user_login_view(request):
	username = request.POST.get('username')



def loginpage(request):
	return render(request,'login_page.html')

def login_view(request):
	cid =request.POST.get('t1')
	print('username',cid)
	pas = request.POST.get('t2')
	print('password',pas)
	custobj = CustomerDetail.objects.filter(customer_id=cid,customer_email=pas).exists()
	if custobj:
		return render(request,'view_login_page.html',{'cid':cid})
	else:
		return render(request,'return_login_page.html')
@login_required
def view_one_customer(request):
	return render(request,'one_customer_detail.html')

@login_required
def get_customer_detail(request,cid):
	cust =request.POST.get('cust_id')
	print('cust id', cid)
	custobj = CustomerDetail.objects.filter(customer_id=cid)
	return render(request,'one_customer.html',{'custobj':custobj})

@login_required
def cust_order(request,cid):
	print('cust_id:',cid)
	ordobj = OrderDetail.objects.filter(customer_data_id=cid)
	return render(request,'getorder.html',{'ordobj':ordobj})





def admin_login(request):
	return render(request,'admin.html')

def admin_view(request):
	userid = request.POST.get('h1')
	password= request.POST.get('h2')
	print('admin id:' ,userid)
	print('admin password:', password)

	if userid =='admin' and password == '1234':
		print('admin login successful')
		return render(request,'admin_view.html')
	else:
		print('Invalid admin')		
		return render(request,'return_admin_login.html')

@login_required
def order_view(request):
	ordobj=OrderDetail.objects.all()
	return render(request,'vieworder.html',{'ordobj':ordobj})



@login_required
def customerdata(request):
	response = HttpResponse(content_type='text/csv')
	response['content-Disposition'] = 'attachment;filename = "customer.csv" '
	cust = CustomerDetail.objects.all()
	print(cust)
	writer = csv.writer(response)
	for ct in cust:
		writer.writerow([ct.customer_id,ct.customer_name,ct.customer_email,ct.customer_phone,ct.customer_address,ct.customer_city,ct.customer_pincode,ct.customer_landmark])
	return response







def categorydatas(request):
	response = HttpResponse(content_type='text/csv')
	response['content-Disposition'] = 'attachment;filename = "category.csv" '
	category = CategoryView.objects.all()
	print(category)
	writer = csv.writer(response)
	for c in category:
		writer.writerow([c.category_id,c.category_name])

	return response



def productdata(request):
	response = HttpResponse(content_type='text/csv')
	response['content-Disposition'] = 'attachment;filename = "product.csv" '
	prod = Products.objects.all()
	print(prod)
	writer = csv.writer(response)
	for pd in prod:
		writer.writerow([pd.product_id,pd.product_name])

	return response

def home_page(request):
	return render(request,'home.html')



# def some_view(request):
# 	buffer = io.BytestID()
# 	p = CustomerDetail.Canvas(buffer)
# 	p.drawstring()
# 	p.showPage()
# 	p.save()
# 	return HttpResponse(buffer,as_attachment=True,filename='hello.pdf')








# def getpdf(request):  
#     response = HttpResponse(content_type='application/pdf')  
#     response['Content-Disposition'] = 'attachment; filename="ct.pdf"' 
#     p = canvas.Canvas(response)  
#     cust= CustomerDetail.objects.all()
#     print(cust)
#     for ct in cust:
#     	cust.drawstring([ct.customer_id,ct.customer_name,ct.customer_email,ct.customer_phone,ct.customer_address,ct.customer_city,ct.customer_pincode,ct.customer_landmark])

#     # p.setFont("Times-Roman", 55)
#     # p.showPage()  
#     # p.save()  
#     return response



# def pdf_view(request):
#     fs = CustomerDetail()
#     filename = 'mypdf.pdf'
#     if fs.exists(filename):
#         with fs.open(filename) as pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
#             return response
#     else:
#         return HttpResponseNotFound('The requested pdf was not found in our server.')  
 
# def admin_category_view(request):
# 	print('category')
# 	cateobj = CategoryView.objects.all()
# 	return render(request,'admin_category_product_view.html',{'cateobj':cateobj})


# def admin_product_category_view(request):
# 	print('hi')
# 	cate =request.POST.get('categoryname')
# 	print('category id  : ', cate)
	
# 	prodobj = Products.objects.filter(category_view_id=cate)
# 	return render(request,'admin_product_view.html',{'prodobj':prodobj})