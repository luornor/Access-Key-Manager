from django.shortcuts import render,redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View
from django.template.loader import render_to_string 
from django.utils.html import strip_tags
from .models import EmailVerification
from .forms import CustomSignUpForm,CustomLoginForm
from .utils import generate_activation_code, send_verification_email, get_code
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


''' HOMEPAGE VIEW '''
class HomeView(TemplateView):
    template_name = 'key_manager/index.html'


class SignUpView(View):
    template_name = 'accounts/signup.html'

    def get(self, request, *args, **kwargs):
        form = CustomSignUpForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self,request, *args,**kwargs):
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False # Deactivate the user until email is verified
            user.save()
            # Generate verification code
            verification_code = generate_activation_code()
            
            # Save the verification code to the database
            EmailVerification.objects.create(user=user, code=verification_code)
            context = {
                "verification_code": verification_code,
            }
            html_message = render_to_string("accounts/email_text.html", context)
            plain_message = strip_tags(html_message)
            # Send verification email
            try:
                # Send verification email
                send_verification_email(user.email, plain_message,html_message) 
                messages.success(request, 'Account created successfully. Please check your email to verify your account.')
                return redirect('verify')
            except Exception as e:
                # Handle the exception if email sending fails
                messages.error(request, f"Error sending email: {e}, please try again.")

                return render(request, self.template_name, {'form': form})
        else:
            print("Form is invalid")
            print(form.errors)
            for error in form.errors.values():
                messages.error(request, error)
            return render(request, self.template_name, {'form': form})


class EmailVerificationView(View):
    template_name = 'accounts/verify_email.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        code = get_code(request)
        try:
            verification = EmailVerification.objects.get(code=code)
            user = verification.user
            if verification.is_expired():
                messages.error(request, "Verification code has expired. Please try again.")
                return redirect('verify')
            user.is_active = True
            user.save()
            verification.delete() 
            messages.success(request, "Account verified successfully. You can now login.")
            return redirect('login')
        
        except EmailVerification.DoesNotExist:
            messages.error(request, "Invalid verification code. Please try again.")
            return redirect('verify')
        
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('verify')


class CustomLoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        form = CustomLoginForm(request.POST)
        return render(request, self.template_name, {'form': form})
    
    def post(self,request, *args,**kwargs):
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                if user.is_staff:
                    return redirect('admin_dashboard')
                else:
                    return redirect('dashboard')
            else:
                messages.error(request, 'Invalid login credentials')
        else:
            messages.error(request, 'Email or password is incorrect')

        context = {
            'form': form,
        }

        return render(request, self.template_name, context)
    
        
class LogoutView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')