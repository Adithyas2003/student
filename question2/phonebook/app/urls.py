from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contactlist'),
    path('add/', views.add_contact, name='add_contact'),
    path('<int:pk>/', views.contact_detail, name='contact_detail'),
    path('<int:pk>/edit/', views.edit_contact, name='edit_contact'),
    path('<int:pk>/delete/', views.delete_contact, name='delete_contact'),
    path('<int:pk>/call/', views.call_contact, name='call_contact'),
]

