from edc_base.views import EdcBaseViewMixin
from edc_dashboard.view_mixins import AppConfigViewMixin

from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView


# from ..mixins import StudySiteNameQuerysetViewMixin
# from .base_listboard import BaseListboardView
app_config = django_apps.get_app_config('edc_pharma_dashboard')
edc_pharma_app_config = django_apps.get_app_config('edc_pharma')


class SubjectDispenseListboardView(EdcBaseViewMixin, AppConfigViewMixin, TemplateView):

    template_name = 'edc_pharma_dashboard/listboard/timeline/timeline.html'
    navbar_name = 'pharma'
    app_config_name = 'edc_pharma_dashboard'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
#         options.update(is_drawn=YES)
        return options
