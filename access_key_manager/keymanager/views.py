from django.views.generic.base import View
from django.http import  JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import AccessKey
from django.contrib import messages
from accounts.models import CustomUser
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import uuid
# Create your views here.

class DashboardView(View):
    template_name = 'key_manager/dashboard.html'

    def get(self, request, *args, **kwargs):
        user_keys = AccessKey.objects.filter(user=request.user)
        context = {
            'user_keys':user_keys,
        }
        return render(request,self.template_name,context)


class AdminDashboardView(View,LoginRequiredMixin,UserPassesTestMixin):
    template_name = 'key_manager/admin_dashboard.html'

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('login')
    
    def get(self, request, *args, **kwargs):
        all_keys = AccessKey.objects.all()
        context = {
            'all_keys':all_keys,
        }
        return render(request, self.template_name, context)
    

class AdminRevokeKeyView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('login')

    def post(self, request, key_id, *args, **kwargs):
        key = get_object_or_404(AccessKey, id=key_id)
        key.status = 'revoked'
        key.save()
        return redirect('admin_dashboard')


class GenerateKeyView(View,LoginRequiredMixin,UserPassesTestMixin):
    
    def test_func(self):
        return not self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect('login')
    template_name = 'key_manager/generate_key.html'


    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if not AccessKey.objects.filter(user=request.user, status='active').exists():
            new_key = AccessKey(
                user=request.user,
                key=str(uuid.uuid4()),
                status='active',
                expiry_date=timezone.now() + timezone.timedelta(days=30)
            )
            new_key.save()
            messages.success(request, 'Access key generated successfully!')
        else:
            messages.error(request, 'You already have an active key.')
        return redirect('dashboard')
    


class KeyStatusApi(View,LoginRequiredMixin):

    def get(self, request, *args, **kwargs):
        email = request.GET.get('email')
        
        if not email:
            return JsonResponse({'error': 'Email parameter is required'}, status=400)

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        active_key = AccessKey.objects.filter(user=user, status='active').first()
        if not active_key:
            return JsonResponse({'error': 'No active key found'}, status=404)
                            
        key_data = {
            'key': active_key.key,
            'key_status': active_key.status,
            'date_procured': active_key.date_procured,
            'expiry_date': active_key.expiry_date,
        }
        return JsonResponse(key_data, status=200)      
