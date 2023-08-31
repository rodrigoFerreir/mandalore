from django.urls import path
from app.api.ViewEntity import ViewEntity
from app.api.ViewProduct import ViewProduct
from app.api.ViewOrder import ViewOrder, ViewAddItemToOrder

urlpatterns = [
    path('entities', ViewEntity.as_view(), name='entities'),
    path('products', ViewProduct.as_view(), name='products'),
    path('orders', ViewOrder.as_view(), name='orders'),
    path('orders/add-item', ViewAddItemToOrder.as_view(), name='add_item_to_order'),
]
