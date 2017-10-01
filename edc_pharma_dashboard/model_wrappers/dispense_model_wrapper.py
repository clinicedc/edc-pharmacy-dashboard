from edc_model_wrapper import ModelWrapper
from edc_pharma.classes import TimepointDescriptor
from edc_pharma.models.dispense_schedule import DispenseSchedule
from edc_pharma.models.dispense_timepoint import DispenseTimepoint

from django.apps import apps as django_apps


app_config = django_apps.get_app_config('edc_pharma_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class DispenseModelWrapper(ModelWrapper):

    model = edc_pharma_app_config.dispense_model
    next_url_name = app_config.dispense_listboard_url_name
    querystring_attrs = ['subject_identifier', 'sid']

    @property
    def dispense_schedule(self):
        try:
            return DispenseSchedule.objects.filter(
                subject_identifier=self.subject_identifier).order_by(
                    'sequence').first()
        except DispenseSchedule.DoesNotExist:
            return None

    @property
    def dispense_timepoint(self):
        if self.dispense_schedule:
            try:
                return DispenseTimepoint.objects.filter(
                    schedule=self.dispense_schedule,
                    is_dispensed=False
                ).order_by('created').first()
            except DispenseTimepoint.DoesNotExist:
                pass

    @property
    def dispense_timepoint_descriptor(self):
        descriptor = TimepointDescriptor(
            dispense_timepoint=self.dispense_timepoint)
        return descriptor
