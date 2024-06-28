from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django import forms
from .models import CustomUser


class CustomSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']
        help_texts = {
            'password1': 'Your password must contain at least 8 characters.',
        }

    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)
        
        # Remove default help texts and add custom styles to each field
        for fieldname in ['email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({
                'class':'w-full py-2 px-3 border-b-1 border-gray-300 bg-gray-300 focus:outline-none focus:border-purple-300',
            })
            if self.fields[fieldname]==self.fields['email']:
                self.fields[fieldname].label  = "Email Address"
                self.fields[fieldname].widget.attrs.update({
                    'placeholder': f'Enter your {fieldname.capitalize()}',
                })

            if self.fields[fieldname]==self.fields['password1']:
                self.fields[fieldname].widget.attrs.update({
                    'placeholder': f'Enter your Password',
                    'data-toggle': 'password'
                })

            if self.fields[fieldname]==self.fields['password2']:
                self.fields[fieldname].label  = "Confirm Password"
                self.fields[fieldname].widget.attrs.update({
                    'placeholder': f'Confirm your Password',
                    'data-toggle': 'password'
                })



class CustomLoginForm(forms.Form):
    email = forms.EmailField(label='Email address',widget=forms.EmailInput(attrs={
        'class': 'w-full py-2 px-3 border-b-1  bg-gray-300 border-purple-300',
        'placeholder': 'Enter your Email',
    }))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={
        'class': 'w-full py-2 px-3 border-b-1 border-gray-300 bg-gray-300 focus:border-purple-300 focus:outline-none',
        'placeholder': 'Enter your Password',
        'data-toggle': 'password'
    }))
    



class StyledPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'shadow-lg appearance-none border rounded w-full py-2 px-3 bg-gray-200  leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': ' Enter Email Address',
        })
    )



class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight mb-5 focus:outline-none focus:shadow-outline',
            'placeholder': 'New Password'
            })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-5 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Confirm New Password'
        })
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''

