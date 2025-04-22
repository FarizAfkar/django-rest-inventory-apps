from django.urls import path
from .views import (
    CreateInventoryAPIView, ListInventoryAPIView, DetailInventoryAPIView,
    UpdateInventoryAPIView, DeleteInventoryAPIView, CustomTokenObtainPairView,
    CustomTokenRefreshView
)

app_name = 'api-inv'

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

    path('inventory/create/', CreateInventoryAPIView.as_view(), name='create-inv'),
    path('inventory/list/', ListInventoryAPIView.as_view(), name='list-inv'),
    path('inventory/detail/<int:id>/', DetailInventoryAPIView.as_view(), name='detail-inv'),
    path('inventory/update/<int:id>/', UpdateInventoryAPIView.as_view(), name='update-inv'),
    path('inventory/delete/<int:id>/', DeleteInventoryAPIView.as_view(), name='delete-inv'),
]
