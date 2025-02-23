from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.core.mail import send_mail
from .models import ServiceRequest
from .forms import ServiceRequestForm, StaffUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django import forms
from django.urls import reverse
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    def get_success_url(self):
        """
        Redirect users based on their is_staff status after login.
        """
        if self.request.user.is_staff:
            return reverse('support_dashboard')  
        else:
            return reverse('submit_request')  

@login_required
def submit_request(request):
    """
    Allows logged-in users to submit a service request.
    """
    if request.user.is_staff:
        return redirect('support_dashboard')  
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user  
            service_request.save()
            return redirect('track_request')  
    else:
        form = ServiceRequestForm()
    return render(request, 'services/submit_request.html', {'form': form})

@login_required
def track_request(request):
    """
    Allows logged-in users to track their service requests.
    """
    if request.user.is_staff:
        return redirect('support_dashboard')  
    requests = ServiceRequest.objects.filter(user=request.user)  
    return render(request, 'services/track_request.html', {'requests': requests})

@login_required
def account_info(request):
    """
    Displays account information for the logged-in user.
    """
    return render(request, 'services/account_info.html')

def is_support_representative(user):
    """
    Checks if the user is a support representative (staff member).
    """
    return user.is_staff

@user_passes_test(is_support_representative)
def support_dashboard(request):
    """
    Displays a dashboard for support representatives to view all service requests.
    """
    requests = ServiceRequest.objects.all()  
    return render(request, 'services/support_dashboard.html', {'requests': requests})

@user_passes_test(is_support_representative)
def update_request_status(request, request_id):
    """
    Allows support representatives to update the status of a service request.
    """
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        remarks = request.POST.get('remarks') 
        service_request.status = new_status
        service_request.remarks = remarks  

        if new_status in ['In Progress', 'Resolved']:
            service_request.reviewed_by = request.user

        if new_status == 'In Progress':
            service_request.action_taken = request.POST.get('action_taken', 'No action details provided.')
            service_request.action_timestamp = timezone.now()

        if new_status == 'Resolved':
            service_request.resolution_date = timezone.now()

        service_request.save()

        notify_user(request, service_request)

        return redirect('support_dashboard')
    return render(request, 'services/update_request_status.html', {'request': service_request})

def signup(request):
    """
    Allows new users to sign up for an account.
    """
    if request.method == 'POST':
        form = StaffUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user) 
            if user.is_staff:
                return redirect('support_dashboard')  
            else:
                return redirect('submit_request')  
    else:
        form = StaffUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def notify_user(request, service_request):
    """
    Sends an email notification to the user when their request status is updated.
    """
    subject = f"Your service request ({service_request.request_type}) has been updated"
    message = (
        f"Status: {service_request.status}\n"
        f"Remarks: {service_request.remarks}\n"  
        f"Resolution Date: {service_request.resolution_date}\n"
        f"Reviewed By: {service_request.reviewed_by.username if service_request.reviewed_by else 'Not yet reviewed'}\n"
        f"Action Taken: {service_request.action_taken if service_request.action_taken else 'No action details provided.'}"
    )
    send_mail(
        subject,
        message,
        'noreply@gasutility.com',  
        [service_request.user.email], 
        fail_silently=False,
    )