from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import DashboardViewMixin

from django import forms
from django.apps import apps as django_apps
from django.contrib import messages
from django.core.management.color import color_style
from django.forms.forms import Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic.base import TemplateView

from .dispense_print_label_mixin import DispensePrintLabelMixin


style = color_style()


class DispenseForm(Form):

    medications = forms.MultipleChoiceField()


app_config = django_apps.get_app_config('edc_pharma_dashboard')


class DispenseViewMixin(DispensePrintLabelMixin):

    def get_success_url(self):
        return '/'

    def post(self, request, *args, **kwargs):
        subject_identifier = kwargs.get('subject_identifier')
        printed_labels = []
        for key in self.request.POST:
            if key.startswith('med'):
                value = self.request.POST.get(key)
                print(
                    value, "{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}")
        if printed_labels:
            msg = 'Successfully printed {}.'.format(
                ', '.join(printed_labels))
            messages.add_message(request, messages.SUCCESS, msg)
        else:
            msg = f'Nothing selected for {subject_identifier}.'
            messages.add_message(request, messages.ERROR, msg)
        url = reverse(
            app_config.appointment_listboard_url_name,
            kwargs={'subject_identifier': subject_identifier})
        return HttpResponseRedirect(url)


class DispensingView(DispenseViewMixin, DashboardViewMixin,
                     EdcBaseViewMixin, TemplateView):
    app_config_name = 'edc_pharma'
