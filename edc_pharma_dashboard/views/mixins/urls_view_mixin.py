from django.apps import apps as django_apps


app_name = 'edc_pharma_dashboard'
app_config = django_apps.get_app_config(app_name)


class UrlsViewMixin:

    prescription_listboard_url_name = app_config.prescription_listboard_url_name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            prescription_listboard_url_name=self.prescription_listboard_url_name,
        )
        return context
