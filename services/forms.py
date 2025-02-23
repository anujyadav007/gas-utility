from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ServiceRequest

class StaffUserCreationForm(UserCreationForm):
    is_staff = forms.BooleanField(
        required=False,
        label="Register as Support Staff",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    ) 
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('is_staff',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = self.cleaned_data['is_staff']
        if commit:
            user.save()
        return user

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attached_files', 'remarks']  # Added 'remarks' field