from __future__ import annotations

from typing import TYPE_CHECKING

from django.apps import apps as django_apps
from edc_device.constants import CLIENT, SERVER

if TYPE_CHECKING:
    from django.db.models import Q


class StudySiteNameQuerysetViewMixin:
    def get_queryset_filter_options(self, request, *args, **kwargs) -> tuple[Q, dict]:
        q_object, options = super().get_queryset_filter_options(request, *args, **kwargs)
        app_config = django_apps.get_app_config("edc_pharmacy")
        if app_config.study_site_name:
            edc_device_app_config = django_apps.get_app_config("edc_device")
            if edc_device_app_config.device_role in [SERVER, CLIENT]:
                options.update(study_site_name=app_config.study_site_name)
        return q_object, options
