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

    dispense_listboard_template_name = 'edc_pharma_dashboard/dispense_listboard.html'
    subject_dispense_listboard_template_name = 'edc_pharma_dashboard/listboard/timeline/timeline.html'

    home_url_name = f'{dashboard_name}:home_url'
    dispense_listboard_url_name = f'{dashboard_name}:dispense_listboard_url'
