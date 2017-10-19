from django.conf import settings

if settings.APP_NAME == 'edc_pharma_dashboard':
    from .tests import models
