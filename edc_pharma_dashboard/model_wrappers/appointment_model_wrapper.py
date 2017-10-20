from edc_model_wrapper import ModelWrapper
from edc_pharma import DispenseAppointmentDescribe
from edc_pharma.models.prescription import Prescription

from django.apps import apps as django_apps


app_config = django_apps.get_app_config('edc_pharma_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class AppointmentModelWrapper(ModelWrapper):

    model = 'edc_pharma.dispenseappointment'
    next_url_name = app_config.appointment_listboard_url_name
    querystring_attrs = ['subject_identifier']

    @property
    def dispense_appt_describe(self):
        return DispenseAppointmentDescribe(dispense_appointment=self.object)

    @property
    def subject_identifier(self):
        return self.object.subject_identifier

    @property
    def prescriptions(self):
        return Prescription.objects.filter(dispense_appointment=self.object)

    @property
    def dispense_appointment_id(self):
        return str(self.object.id)

    @property
    def can_dispense_labels(self):
        if self.object.previous():
            return self.object.previous().is_dispensed
        return True
