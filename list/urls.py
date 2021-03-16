from django.urls import path
from . import views

urlpatterns = [
    path('Dashboard/', views.Dashboard, name='employee_detail'),  # 3
    path(''
         '', views.feed, name='firstpage'),  # 3
    path('update/<str:pk>/', views.update_Employee, name='update'),#update
    path('delete/<str:pk>/', views.delete_Employee, name='delete'),#delete
    path('customer/', views.customer, name="customer"),

]
