from edc_model_wrapper import ModelWrapper
from edc_pharma import DispenseAppointmentDescibe
from edc_pharma.medications import Medication
from edc_pharma.medications import medications

from django.apps import apps as django_apps


app_config = django_apps.get_app_config('edc_pharma_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class DispenseAppointmentModelWrapper(ModelWrapper):

    model = 'edc_pharma.dispenseappointment'
    next_url_name = app_config.dispense_listboard_url_name
    querystring_attrs = ['subject_identifier']

    @property
    def dispense_appt_describe(self):
        return DispenseAppointmentDescibe(dispense_appointment=self.object)

    @property
    def patient_history(self):
        pass

    @property
    def medications(self):
        _medications = []
        body_weight = 32.0
        duration = self.dispense_appt_describe.duration
        for med in self.object.profile_medications:
            medication_definition = medications.get(med.name)
            medication = Medication(
                medication_definition=medication_definition, weight=body_weight,
                duration=duration)
            _medications.append(medication)
        return _medications

    @property
    def dispense_timepoint_id(self):
        return str(self.object.id)

    @property
    def can_dispense_labels(self):
        if self.object.previous():
            return self.object.previous().is_dispensed
        return True
