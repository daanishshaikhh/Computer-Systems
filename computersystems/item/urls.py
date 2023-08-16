from django.urls import path
from . import views

app_name = 'laptop'
urlpatterns=[
    path('<str:pk>/', views.detail, name='detail'),
]