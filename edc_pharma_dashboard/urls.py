# coding=utf-8

from django.conf.urls import url, include

from edc_pharma_dashboard.views.action_views.dispense_view import DispenseView
from edc_pharma_dashboard.views.home_view import HomeView
from edc_pharma_dashboard.views.listboard_views.dispense_listboard_view import DispenseListboardView


# from edc_pharma_dashboard.views.action_views.dispense_view import (
#     DispenseView)
# from .views import ListBoardView, LocationView
app_name = 'edc_pharma_dashboard'

urlpatterns = [
    url(r'^tz_detect/', include('tz_detect.urls')),
    #     url(r'login', LoginView.as_view(), name='login_url'),
    #     url(r'logout', LogoutView.as_view(
    #         pattern_name='login_url'), name='logout_url'),
    url(r'^listboard/dispense/$', DispenseListboardView.as_view(),
        name='dispense_listboard_url'),
    url(r'^pharma/$', DispenseView.as_view(), name='dispense_url'),
    url(r'', HomeView.as_view(), name='home_url'),
]
