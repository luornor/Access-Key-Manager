from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('admin-dashboard/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('generate-key/', views.GenerateKeyView.as_view(), name='generate_key'),
    path('admin-revoke-key/<int:key_id>/', views.AdminRevokeKeyView.as_view(), name='admin_revoke_key'),
    path('key-status/', views.KeyStatusApi.as_view(), name='key_status'),
]

