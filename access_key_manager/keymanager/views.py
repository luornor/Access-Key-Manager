from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

class DashboardView(View):
    template_name = 'key_manager/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        pass


class AdminDashboardView(View):
    template_name = 'key_manager/admin_dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        pass