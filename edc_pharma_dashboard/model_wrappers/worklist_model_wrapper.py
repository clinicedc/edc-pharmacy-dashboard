from edc_model_wrapper import ModelWrapper
from edc_pharma.models.dispense_appointment import DispenseAppointment

from django.apps import apps as django_apps


app_config = django_apps.get_app_config('edc_pharma_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class WorklistModelWrapper(ModelWrapper):

    model = edc_pharma_app_config.worklist_model
    next_url_name = app_config.worklist_listboard_url_name
    querystring_attrs = ['subject_identifier']

    @property
    def subject_identifier(self):
        return self.object.subject_identifier

    @property
    def appointments(self):
        return [appt.is_dispensed for appt in DispenseAppointment.objects.filter(
            subject_identifier=self.subject_identifier)]
