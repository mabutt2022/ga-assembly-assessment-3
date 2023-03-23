from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('form/<int:widget_id>/', views.delete_item, name='delete'),
    ]
