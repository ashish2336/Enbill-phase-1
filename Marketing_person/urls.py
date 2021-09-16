"""Marketing_person URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from APIVIEW import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Marketing/', views.Marketing_ProfileAPI.as_view()),
    path('Marketing/<int:pk>/', views.Marketing_ProfileAPI.as_view()),
    path('Add_items/', views.Add_itemsAPI.as_view()),
    path('Add_items/<int:pk>/', views.Add_itemsAPI.as_view()),
    path('Create_bill/', views.Create_billAPI.as_view()),
    path('Create_bill/<int:pk>/', views.Create_billAPI.as_view()),
    path('Catelog/', views.CatelogAPI.as_view()),
    path('Catelog/<int:pk>/', views.CatelogAPI.as_view()),
    path('Sales_team/', views.Sales_teamAPI.as_view()),
    path('Sales_team/<int:pk>/', views.Sales_teamAPI.as_view()),
    path('Customer_Profile/', views.Customer_ProfileAPI.as_view()),
    path('Customer_Profile/<int:pk>/', views.Customer_ProfileAPI.as_view()),
    path('Profile/', views.ProfileAPI.as_view()),
    path('Profile/<int:pk>/', views.ProfileAPI.as_view()),

]