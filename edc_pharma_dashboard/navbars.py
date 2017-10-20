from edc_base import NavbarItem

navbar_items = []
config = [
    ('edc_pharma_dashboard', 'prescription', 'Prescriptions', None,
     'prescription_listboard_url_name'),
    ('edc_pharma_dashboard', 'appointment', 'Dispensing', None,
     'appointment_listboard_url_name'),
    ('edc_pharma_dashboard', 'home', '', 'fa-medkit', 'home_url_name')
]
for app_config_name, name, label, fa_icon, app_config_attr in config:
    navbar_item = NavbarItem(
        app_config_name=app_config_name,
        name=name,
        label=label,
        fa_icon=fa_icon,
        app_config_attr=app_config_attr)
    navbar_items.append(navbar_item)
