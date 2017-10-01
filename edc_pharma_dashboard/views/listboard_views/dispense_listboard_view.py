from edc_constants.constants import YES

from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from edc_pharma_dashboard.model_wrappers.dispense_model_wrapper import DispenseModelWrapper

from ..listboard_filters import DispenseListboardViewFilters
from ..mixins import StudySiteNameQuerysetViewMixin
from .base_listboard import BaseListboardView


app_config = django_apps.get_app_config('edc_pharma_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class DispenseListboardView(StudySiteNameQuerysetViewMixin, BaseListboardView):

    navbar_item_selected = 'dispense'

    model = edc_pharma_app_config.dispense_model
    model_wrapper_cls = DispenseModelWrapper
    listboard_url_name = app_config.dispense_listboard_url_name
    listboard_template_name = app_config.dispense_listboard_template_name
    show_all = True
    listboard_view_filters = DispenseListboardViewFilters()
    form_action_url_name = f'edc_pharma_dashboard:dispense_url'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
#         options.update(is_drawn=YES)
        return options
