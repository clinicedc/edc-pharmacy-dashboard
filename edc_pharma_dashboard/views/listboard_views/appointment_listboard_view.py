from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from edc_pharma_dashboard.model_wrappers import AppointmentModelWrapper
from edc_pharma_dashboard.views.listboard_filters import AppointmentListboardViewFilters

from .base_listboard import BaseListboardView


app_config = django_apps.get_app_config('edc_pharma_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class AppointmentListboardView(BaseListboardView):

    navbar_item_selected = 'appointment'

    model = edc_pharma_app_config.dispense_appointment_model
    model_wrapper_cls = AppointmentModelWrapper
    form_action_url_name = f'edc_pharma_dashboard:dispensing_action_url'
    listboard_url_name = app_config.appointment_listboard_url_name
    prescription_listbord_url_name = app_config.prescription_listboard_url_name
    listboard_template_name = app_config.appointment_listboard_template_name
    show_all = True
    listboard_view_filters = AppointmentListboardViewFilters()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            listboard_url_name=self.listboard_url_name,
            dispense_listbord_url_name=self.prescription_listbord_url_name,
            dispensing_form_url_name=app_config.dispensing_form_url_name)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('subject_identifier'):
            options.update(schedule__subject_identifier=kwargs.get(
                'subject_identifier'))
        return options
