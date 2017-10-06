from edc_label.print_server import PrintServerSelectPrinterError
from edc_pharma.dispense import Dispense

from django.apps import apps as django_apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.utils.decorators import method_decorator

from .base_action_view import BaseActionView


app_config = django_apps.get_app_config('edc_pharma_dashboard')


class DispenseView(BaseActionView):

    post_url_name = app_config.dispense_listboard_url_name
    valid_form_actions = ['print_labels']
    action_name = 'pharma'

    dispense_cls = Dispense

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.print_labels(request, **kwargs)
        return HttpResponseRedirect(self.post_url)

    def print_labels(self, request, **kwargs):
        try:
            print(request.user.__dict__, "request.user request.user request.user")
            dispense_print = self.dispense_cls(
                user=request.user,
                subject_identifier=kwargs.get('subject_identifier'),
                timepoint_id=kwargs.get('timepoint'))
        except PrintServerSelectPrinterError as e:
            messages.error(
                self.request,
                str(e), extra_tags='PrintServerSelectPrinterError')
        else:
            for label in dispense_print.printed_labels or []:
                description = label.get('medication')
                subject_identifier = label.get('subject_identifier')
                messages.success(
                    self.request,
                    f'Printed {description} for {subject_identifier}.')
