from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import secrets


def generate_activation_code():
    return ''.join([str(secrets.randbelow(10)) for _ in range(6)])


def send_verification_email(email,message,html_message):

    try:
        subject = 'Verify your email'
        from_email = settings.EMAIL_HOST_USER
        msg = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=from_email,
            to=[email],)
        msg.attach_alternative(html_message, 'text/html')
        msg.send()
    except Exception as e:
        print(f"Error sending email: {e}")
        raise e 


def get_code(request):
    try:
        code = (
            (request.POST.get("input1") or '') +
            (request.POST.get("input2") or '') +
            (request.POST.get("input3") or '') +
            (request.POST.get("input4") or '') +
            (request.POST.get("input5") or '') +
            (request.POST.get("input6") or '')
        )
        if not code.isdigit():
            raise ValueError("Verification code must be numeric.")
        return int(code)
    except ValueError as e:
        raise ValueError("Invalid verification code.")