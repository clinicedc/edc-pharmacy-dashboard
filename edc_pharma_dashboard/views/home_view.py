from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import AppConfigViewMixin

from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

app_config = django_apps.get_app_config('edc_pharma_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class HomeView(EdcBaseViewMixin, AppConfigViewMixin, TemplateView):

    template_name = 'edc_pharma_dashboard/home.html'
    navbar_name = 'pharma'
    app_config_name = 'edc_pharma_dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            base_template_name=self.base_template_name,
            randomized_subjects_url=app_config.prescription_listboard_url_name,
            dispense_appt_subjects_url=app_config.dispense_appointment_listboard_url_name,
        )
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
