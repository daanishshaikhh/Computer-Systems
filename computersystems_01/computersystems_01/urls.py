from django.contrib import admin
from django.urls import path, include
from core.views import index, contact, signup, login_view, laptop_list, user_home, user_buy, user_repair, admin_home, admin_receipts, admin_laptops, admin_employees, admin_add_technician, admin_add_laptop
from core.views import admin_all_technicians
urlpatterns = [
    path('', index, name='index'),
    path('laptops/',include('laptop.urls')),
    path('contact/',contact, name='contact'),
    path('available/', laptop_list, name='laptop_list'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('user_home/', user_home ,name='user_home'),
    path('admin_home/', admin_home ,name='admin_home'),
    path('admin_receipts/', admin_receipts ,name='admin_receipts'),
    path('admin_laptops/', admin_laptops ,name='admin_laptops'),
    path('admin_employees/', admin_employees ,name='admin_employees'),
    path('admin_add_technician/', admin_add_technician ,name='admin_add_technician'),
    path('admin_all_technicians/', admin_all_technicians ,name='admin_all_technicians'),
    path('admin_add_laptop/', admin_add_laptop ,name='admin_add_laptop'),
    path('user_buy/', user_buy ,name='user_buy'),
    path('user_repair/', user_repair ,name='user_repair'),
    path('admin/', admin.site.urls),
]