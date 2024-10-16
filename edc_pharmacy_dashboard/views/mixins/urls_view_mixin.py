from typing import Any

from django.apps import apps as django_apps

app_name = "edc_pharmacy_dashboard"
app_config = django_apps.get_app_config(app_name)


class UrlsViewMixin:
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        kwargs.update(prescribe_listboard_url_name=app_config.prescribe_listboard_url_name)
        return super().get_context_data(**kwargs)
