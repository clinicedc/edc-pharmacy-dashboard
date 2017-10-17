# coding=utf-8

from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edc_pharma_dashboard'
    url_namespace = 'edc_pharma_dashboard'
    admin_site_name = 'edc_pharma_admin'
    dashboard_name = 'edc_pharma_dashboard'
    base_template_name = 'edc_base/base.html'
    listboard_url_name = f'{dashboard_name}:dispense_listboard_url'
    dashboard_url_name = 'home_url'

    prescription_listboard_template_name = 'edc_pharma_dashboard/prescription_listboard.html'
    dispense_appointment_listboard_template_name = 'edc_pharma_dashboard/dispenseappointment_listboard.html'
    home_url_name = f'{dashboard_name}:home_url'
    prescription_listboard_url_name = f'{dashboard_name}:prescription_listboard_url'
    dispense_appointment_listboard_url_name = f'{dashboard_name}:dispenseappointment_listboard_url'
    dispensing_form_url_name = f'{dashboard_name}:dispensing_form_url'
