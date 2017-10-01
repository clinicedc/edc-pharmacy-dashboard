from edc_dashboard.listboard_filter import ListboardFilter, ListboardViewFilters


class DispenseListboardViewFilters(ListboardViewFilters):

    all = ListboardFilter(
        name='all',
        position=0,
        label='All',
        lookup={})

    missed = ListboardFilter(
        name='control',
        position=10,
        label='control',
        lookup={'missed': True})

    previous = ListboardFilter(
        label='singledose',
        position=20,
        lookup={'singledose': True})
