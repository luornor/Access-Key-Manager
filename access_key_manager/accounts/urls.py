from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('verify-email/', views.EmailVerificationView.as_view(), name='verify'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]

