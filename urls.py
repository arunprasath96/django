"""shoppingapp URL Configuration

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

from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include
from jabong import views
from jabong.views import productdetail
from jabong.views import customer_insert
from jabong.views import category_product
from jabong.views import create_one_category
from jabong.views import create_one_product
from jabong.views import view_customer
# from jabong.views import order_masterpage
from jabong.views import order_detail_page
from jabong.views import customer_create_form,customer_edit,customer_delete
from jabong.views import product_create_form,edit_product,product_delete
from jabong.views import order_form,edit_order,order_delete
from .views import thanks
from .views import home, register
from .views import user_login
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url








urlpatterns = [



	path('',views.index,name='index'),
    path('create_category/',create_one_category.as_view(),name='create_category'),
    path('category_view',category_product.as_view(),name='category_view'),

    path('view_prod/',views.view_products,name='view_prod'),
    path('create_product/',create_one_product.as_view(),name='create_product'),
    path('view_all_product/',productdetail.as_view(),name='view_all_product'),
    path('product_insert/',views.add_product,name='product_insert'),

    
    path('create_customer/',customer_insert.as_view(),name='create_customer'),
    path('customer_view/',view_customer.as_view(),name='customer_view'),
    path('insert_customer/',views.add_customer,name='insert_customer'),
    path('reg_customer/',views.customer_portal,name='reg_customer'),


    # path('order_page/',order_masterpage.as_view(),name='order_page'),
    path('order_detail_page/',order_detail_page.as_view(),name='order_detail_page'),


    path('product_order/',views.add_order,name='product_order'),
    path('view_order_page/',views.view_order,name='view_order_page'),

    path('view_one_order/',views.view_one_order,name='view_one_order'),
	path('getorder/',views.get_one_order,name='getorder'),
    path('customer_order/<int:cid>',views.cust_order,name='customer_order'),

    path('one_customer/',views.view_one_customer,name='one_customer'),
    path('one_customer_detail/<int:cid>',views.get_customer_detail,name='one_customer_detail'),



    path('login_page/',views.loginpage,name='login_page'),
    path('view_login_page/',views.login_view,name='view_login_page'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_view/',views.admin_view,name='admin_view'),

    # path('user_loginpage/',views.user_loginpage,name='user_loginpage'),
    # path('view_user_login/',views.my_view,name='view_user_login'),

    





    path('category_pord/',views.category_view,name='category_pord'),
    path('product_category/',views.product_category_view,name='product_category'),
    path('orderpage/',views.order_page,name='orderpage'),


    path('order_prod/<int:order_prod>',views.order_page,name='order_prod'),
    path('palce_order/',views.order_placed,name='palce_order'),

    path('order_view/',views.order_view,name='order_view'),

    path('filecsv/',views.customerdata,name='csv'), 
    path('categorycsv/',views.categorydatas,name='categorycsv'), 
    path('productcsv/',views.productdata,name='productcsv'), 

    # path('pdf_view/',views.some_view,name='pdf_view'), 

   

    path('customer_create_form/',views.customer_create_form,name='customer_create_form'),
    path('customer_edit/<int:pk>/',views.customer_edit,name='customer_edit'),
    path('customer_delete/<int:pk>/',views.customer_delete,name='customer_delete'),

    path('product_create_form/',views.product_create_form,name='product_create_form'),
    path('edit_product/<int:pk>/',views.edit_product,name='edit_product'),
    path('product_delete/<int:pk>/',views.product_delete,name='product_delete'),

    
    path('order_form/',views.order_form,name='order_form'),
    path('edit_order/<int:pk>/',views.edit_order,name='edit_order'),
    path('order_delete/<int:pk>/',views.order_delete,name='order_delete'),

    path('homepage/',views.home_page,name='homepage'),


    path('thanks/',views.thanks,name='thanks'),

    # path('register', views.RegisterView.as_view(), name='register'),


    path('user_register/',views.register,name='user_rigester'),
    path('user_home/',views.home,name='user_home'),

    # path('user_home/',views.user_auth,name='user_home'),


    # path("login", views.login_request, name="login"),

    # url(r'^logout/$', auth_views.logout)

    path('login/',user_login.as_view(),name='login'),
    path('logoutpage/', auth_views.LogoutView.as_view(template_name='user_home.html'),name='logoutpage'),
    path('signup/',views.signup, name='signup'),

    # path('signup2/', views.signup_view, name='signup'),
    # path('login7/', views.login_view2, name='login')



]
    # path('api_token_auth/', CustomAuthToken.as_view(),name='api_token_auth'),

# path('login/', auth_views.LoginView.as_view(template_name='user_register.html'),
   #     name='login'
   # )
   






     # path('product_insert/',views.add_product,name='product_insert'),
    # path('category_insert/',views.add_category,name='category_insert'),

    # path('reg_customer/',views.customer_portal,name='reg_customer'),
    # path('admin_category_porduct/',views.admin_category_view,name='admin_category_pord'),
    # path('admin_product_category/',views.admin_product_category_view,name='admin_product_category'),
    
    # path('file/',views.getfile,name='file'), 


