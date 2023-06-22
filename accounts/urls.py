from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create_order/', views.CreateOrder, name='create_order'),
    path('update_order/<str:pk>/', views.UpdateOrder, name='update_order'),
    path('delete_order/<str:pk>', views.DeleteOrder, name='delete_order'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logoutPage'),
]
