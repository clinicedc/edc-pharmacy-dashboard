from edc_model_wrapper import ModelWrapper
from edc_pharma.models import DispenseSchedule
from edc_pharma.models.dispense_timepoint import DispenseTimepoint

from django.apps import apps as django_apps


app_config = django_apps.get_app_config('edc_pharma_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class DispenseTimepointModelWrapper(ModelWrapper):

    model = edc_pharma_app_config.dispense_timepoint_model
    next_url_name = app_config.dispense_listboard_url_name

    @property
    def dispense_schedule(self):
        try:
            return DispenseSchedule.objects.get(
                identifier=self.subject_identifier
            ).order_by('created').first()
        except DispenseSchedule.DoesNotExist:
            return None

    @property
    def dispense_timepoint(self):
        dispense_timepoint = None
        if self.dispense_schedule:
            try:
                dispense_timepoint = DispenseTimepoint.objects.get(
                    schedule=self.dispense_schedule)
            except DispenseTimepoint.DoesNotExist:
                pass
        return dispense_timepoint
