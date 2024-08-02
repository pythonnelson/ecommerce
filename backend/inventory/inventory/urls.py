from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('UserServices.urls', namespace='users')),
    path('products/', include('ProductServices.urls', namespace='products')),
    path('orders/', include('OrderServices.urls', namespace='orders')),
    path('inventory/', include('InventoryServices.urls', namespace='inventories')),
]
