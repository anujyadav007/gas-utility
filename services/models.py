from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('Gas Leak', 'Gas Leak'),
        ('Meter Reading', 'Meter Reading'),
        ('Billing Issue', 'Billing Issue'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_requests')
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    submission_date = models.DateTimeField(auto_now_add=True)
    resolution_date = models.DateTimeField(null=True, blank=True)
    attached_files = models.FileField(upload_to='attachments/', null=True, blank=True, verbose_name='Attached Files')
    action_taken = models.CharField(max_length=255, blank=True, null=True)
    action_timestamp = models.DateTimeField(null=True, blank=True)  
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_requests')
    remarks = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"{self.user.username} - {self.request_type}"