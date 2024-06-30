from django.urls import path
from .import views
from django.contrib.auth.views import PasswordResetCompleteView,PasswordResetDoneView


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('verify-email/', views.EmailVerificationView.as_view(), name='verify'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_reset/', views.CustomPasswordResetView.as_view(
        template_name='accounts/password_reset_form.html'),
        name='password_reset'),

    path('reset/<uidb64>/<token>/',views.CustomPasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),

    path('password_reset/done/',PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),

    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
]

