from django.core.mail import send_mail
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

@receiver(user_logged_in)
def send_login_email(sender, request, user, **kwargs):
    subject = 'Welcome Back to Gas Utility Service'
    message = f'Hi {user.username},\n\nYou have successfully logged in to your account.\n\nBest regards,\nThe Gas Utility Team'
    from_email = 'noreply@gasutility.com'
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)