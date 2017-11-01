from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import AppConfigViewMixin

app_config = django_apps.get_app_config('edc_pharmacy_dashboard')
edc_pharmacy_app_config = django_apps.get_app_config('edc_pharmacy')


class HomeView(EdcBaseViewMixin, AppConfigViewMixin, TemplateView):

    template_name = 'edc_pharmacy_dashboard/home.html'
    navbar_name = 'pharma'
    app_config_name = 'edc_pharmacy_dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            base_template_name=self.base_template_name,
            prescription_listboard_url=app_config.prescription_listboard_url_name,
            # dispense_appt_subjects_url=app_config.appointment_listboard_url_name,
        )
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
