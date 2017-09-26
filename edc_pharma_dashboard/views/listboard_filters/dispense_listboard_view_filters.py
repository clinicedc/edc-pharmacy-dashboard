from edc_dashboard.listboard_filter import ListboardFilter, ListboardViewFilters
from edc_lab.models import BoxItem


def get_box_items():
    return BoxItem.objects.all().values('identifier')


class RequisitionListboardViewFilters(ListboardViewFilters):

    all = ListboardFilter(
        name='all',
        position=0,
        label='All',
        lookup={})

    missed = ListboardFilter(
        name='missed',
        position=10,
        label='Missed',
        lookup={'missed': True})

    due_today = ListboardFilter(
        label='due_today',
        position=20,
        lookup={'previous': True})

    previous = ListboardFilter(
        label='previous',
        position=30,
        lookup={'previous': True})

    control = ListboardFilter(
        label='control',
        position=40,
        lookup={'Control': True})

    single_dose = ListboardFilter(
        label='Enrolled',
        position=50,
        lookup={'enrolled': True})s
