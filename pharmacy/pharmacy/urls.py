from django.contrib import admin
from django.urls import path, include
from edc_base.views import LoginView, LogoutView
from edc_pharmacy.admin_site import edc_pharmacy_admin

from .views import HomeView, AdministrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', edc_pharmacy_admin.urls),
    path('tz_detect/', include('tz_detect.urls')),
    path('login', LoginView.as_view(), name='login_url'),
    path('logout', LogoutView.as_view(
        pattern_name='login_url'), name='logout_url'),
    path('admininistration/', AdministrationView.as_view(),
         name='administration_url'),
    path('edc/', include('edc_base.urls')),
    path('edc_protocol/', include('edc_protocol.urls')),
    path('edc_label/', include('edc_label.urls')),
    path('edc_pharmacy/', include('edc_pharmacy.urls')),
    path('pharmacy/', include('edc_pharmacy_dashboard.urls')),
    path('admininistration/', HomeView.as_view(manual_revision='1.0'),
         name='subject_models_url'),
    path('home/', HomeView.as_view(manual_revision='1.0'), name='home_url'),
    path('', HomeView.as_view(manual_revision='1.0'), name='home_url'),
]
