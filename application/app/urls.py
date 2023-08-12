from django.urls import path
from app.api.ViewEntity import ViewEntity

urlpatterns = [
    path('entities', ViewEntity.as_view(), name='entities'),

]
