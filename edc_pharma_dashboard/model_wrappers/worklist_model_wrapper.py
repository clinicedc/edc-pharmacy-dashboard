from edc_model_wrapper import ModelWrapper

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
    def is_pending(self):
        return (
            self.dispense_appt_describe.is_next_pending_appointment()
            and not self.object.is_approved)
