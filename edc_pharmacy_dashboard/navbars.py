from edc_navbar import NavbarItem, site_navbars, Navbar

url_namespace = 'edc_pharmacy_dashboard'

pharmacy_dashboard = Navbar(name='pharmacy_dashboard')


pharmacy_dashboard.append_item(
    NavbarItem(name='prescribe',
               title='Prescribe',
               label='prescribe',
               glyphicon='glyphicon-edit',
               url_name=f'{url_namespace}:prescribe_listboard_url'))

pharmacy_dashboard.append_item(
    NavbarItem(name='dispense',
               title='Dispense',
               label='dispense',
               glyphicon='glyphicon-share',
               url_name=f'{url_namespace}:dispense_listboard_url'))

pharmacy_dashboard.append_item(
    NavbarItem(name='pharmacy',
               fa_icon='fa-medkit',
               url_name=f'{url_namespace}:home_url'))


site_navbars.register(pharmacy_dashboard)
