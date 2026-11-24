from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.company, name='company'),
    path('customers/', views.customer, name='customers'),
    path('customers/new/', views.customernew, name='new'),
    path('customers/update/<int:pk>', views.customerupdate, name='update'),
    path('customers/delete/<int:pk>', views.customerdelete, name='delete'),
]
