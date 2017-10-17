from edc_dashboard.listboard_filter import ListboardFilter, ListboardViewFilters


class DispenseAppointmentListboardViewFilters(ListboardViewFilters):

    all = ListboardFilter(
        name='all',
        position=0,
        label='All',
        lookup={})

    not_dispensed = ListboardFilter(
        name='control_arm',
        position=10,
        label='Control Arm',
        lookup={'rx': True})

    dispensed = ListboardFilter(
        name='rx',
        label='Single Dose',
        position=20,
        lookup={'singledose': True})
