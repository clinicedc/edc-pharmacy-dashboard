from edc_model_wrapper import ModelWrapper
from edc_pharma.timepoint_descriptor import TimepointDescriptor

from django.apps import apps as django_apps


app_config = django_apps.get_app_config('edc_pharma_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class DispenseTimepointModelWrapper(ModelWrapper):

    model = 'edc_pharma.dispensetimepoint'
    next_url_name = app_config.dispense_listboard_url_name
    querystring_attrs = ['subject_identifier']

    @property
    def descriptor(self):
        return TimepointDescriptor(dispense_timepoint=self.object)

    @property
    def dispense_timepoint_id(self):
        return str(self.object.id)
