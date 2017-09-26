

class DispenseQuerysetViewMixin:

    subject__queryset_lookups = []

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = {}
        return options

    def get_queryset_exclude_options(self, request, *args, **kwargs):
        options = {}
        return options
