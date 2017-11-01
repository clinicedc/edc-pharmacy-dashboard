from django.conf import settings

if settings.APP_NAME == 'edc_pharmacy_dashboard':
    from .tests import models
