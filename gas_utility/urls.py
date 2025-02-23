from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView  # Import LogoutView
from services.views import (
    signup, submit_request, track_request, account_info,
    support_dashboard, update_request_status, CustomLoginView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('services.urls')),  # Include services app URLs
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Use custom login view
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs
    path('signup/', signup, name='signup'),  # Signup URL
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Logout URL
    path('', RedirectView.as_view(url='services/submit-request/')),  # Redirect root URL to submit_request
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

