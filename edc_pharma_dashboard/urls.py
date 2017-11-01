# coding=utf-8

from edc_constants.constants import UUID_PATTERN

from django.conf.urls import url, include

from edc_pharmacy_dashboard.views import HomeView, DispensingView
from edc_pharmacy_dashboard.views.action_views import (
    ApprovePrescriptionView, DispensePrintLabelActionView, DispensingActionView)
from edc_pharmacy_dashboard.views.listboard_views import (
    AppointmentListboardView, PrescriptionListboardView, WorklistListboardView)

from .patterns import subject_identifier
from edc_base.views import LoginView, LogoutView
from django.conf import settings


app_name = 'edc_pharmacy_dashboard'


urlpatterns = [
    url(r'^listboard/prescription/$', PrescriptionListboardView.as_view(),
        name='prescription_listboard_url'),
    url(r'^listboard/worklist/$', WorklistListboardView.as_view(),
        name='worklist_listboard_url'),
    url(r'^listboard/dispensing/$', AppointmentListboardView.as_view(),
        name='appointment_listboard_url'),
    url(r'^prescription/approve/$', ApprovePrescriptionView.as_view(),
        name='approve_prescription_url'),
    url(r'^listboard/dispensing/$', DispensingActionView.as_view(),
        name='dispensing_action_url'),
    url(r'^listboard/dispensing/'
        '(?P<subject_identifier>' + subject_identifier + ')/'
        '(?P<appointment>' + UUID_PATTERN.pattern + ')/',
        DispensePrintLabelActionView.as_view(),
        name='dispense_print_label_action_url'),
    url(r'^listboard/dispensing/'
        '(?P<subject_identifier>' + subject_identifier + ')/',
        AppointmentListboardView.as_view(),
        name='appointment_listboard_url'),
    url(r'^dashboard/dispensing/'
        '(?P<subject_identifier>' + subject_identifier + ')/'
        '(?P<appointment>' + UUID_PATTERN.pattern + ')/',
        DispensingView.as_view(), name='dispensing_form_url'),
    url(r'^listboard/prescription/'
        '(?P<subject_identifier>' + subject_identifier + ')/',
        PrescriptionListboardView.as_view(),
        name='prescription_listboard_url'),
    # url(r'', HomeView.as_view(), name='home_url'),
]


# if settings.APP_NAME == 'edc_pharmacy_dashboard':
#     urlpatterns += [
#         url(r'login', LoginView.as_view(), name='login_url'),
#         url(r'logout', LogoutView.as_view(
#             pattern_name='login_url'), name='logout_url'),
#     ]
