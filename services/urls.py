from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('submit-request/', views.submit_request, name='submit_request'),  
    path('track-request/', views.track_request, name='track_request'),  
    path('account/', views.account_info, name='account_info'),  

    
    path('support/dashboard/', views.support_dashboard, name='support_dashboard'),  
    path('support/update-status/<int:request_id>/', views.update_request_status, name='update_request_status'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)