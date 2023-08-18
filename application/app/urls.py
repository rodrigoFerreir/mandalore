from django.urls import path
from app.api.ViewEntity import ViewEntity
from app.api.ViewProduct import ViewProduct

urlpatterns = [
    path('entities', ViewEntity.as_view(), name='entities'),
    path('products', ViewProduct.as_view(), name='products'),

]
