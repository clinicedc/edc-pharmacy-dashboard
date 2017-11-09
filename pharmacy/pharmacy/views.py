from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin, AdministrationViewMixin
from edc_dashboard.view_mixins import AppConfigViewMixin
from edc_navbar import NavbarViewMixin


class HomeView(EdcBaseViewMixin, NavbarViewMixin, AppConfigViewMixin, TemplateView):

    template_name = 'pharmacy/home.html'
    app_config_name = 'pharmacy'

    navbar_name = 'pharmacy'
    navbar_selected_item = 'home'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AdministrationView(EdcBaseViewMixin, AdministrationViewMixin, NavbarViewMixin,
                         AppConfigViewMixin, TemplateView):

    base_template_name = 'pharmacy/base.html'
    app_config_name = 'pharmacy'

    navbar_name = 'pharmacy'
    navbar_selected_item = 'administration'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
