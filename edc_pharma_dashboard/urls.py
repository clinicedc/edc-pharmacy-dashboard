# coding=utf-8

from edc_constants.constants import UUID_PATTERN

from django.conf.urls import url, include

from edc_pharma_dashboard.views import DispenseListboardView
from edc_pharma_dashboard.views import SubjectDispenseListboardView
from edc_pharma_dashboard.views.action_views.dispense_view import DispenseView
from edc_pharma_dashboard.views.home_view import HomeView
from edc_pharma_dashboard.views.listboard_views.dispensetimepoint_listboard_view import DispenseTimepointListboardView

from .patterns import subject_identifier


app_name = 'edc_pharma_dashboard'


urlpatterns = [
    url(r'^tz_detect/', include('tz_detect.urls')),
    #     url(r'login', LoginView.as_view(), name='login_url'),
    #     url(r'logout', LogoutView.as_view(
    #         pattern_name='login_url'), name='logout_url'),
    url(r'^listboard/dispense/$', DispenseListboardView.as_view(),
        name='dispense_listboard_url'),
    url(r'^listboard/dispensetimepoint/$', DispenseTimepointListboardView.as_view(),
        name='dispensetimepoint_listboard_url'),
    url(r'^listboard/dispense/'
        '(?P<subject_identifier>' + subject_identifier + ')/'
        '(?P<timepoint>' + UUID_PATTERN.pattern + ')/',
        DispenseView.as_view(),
        name='dispense_listboard_url'),

    url(r'^timeline/$', SubjectDispenseListboardView.as_view(),
        name='subject_dispense_listboard_url'),
    url(r'^pharma/$', DispenseView.as_view(), name='dispense_url'),
    url(r'', HomeView.as_view(), name='home_url'),
]
