from django.urls import path
from .views import ProductListView, ServicesListView, UserListView
from . import views

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/add/', views.add_product, name='add_product'),
    path('api/services/', ServicesListView.as_view(), name = 'services_list'),
    path('api/services/add/', views.add_service, name = 'add_service'),
    path('api/users/', UserListView.as_view(), name = 'user-list'),
    path('api/users/add/', views.add_user, name = 'add-user')
]