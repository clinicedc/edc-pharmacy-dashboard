from edc_navbar import NavbarItem, site_navbars, Navbar

pharmacy = Navbar(name='pharmacy')

pharmacy.append_item(
    NavbarItem(name='pharmacy',
               title='Pharmacy',
               label='pharmacy',
               fa_icon='fa-medkit',
               url_name=f'edc_pharmacy_dashboard:home_url'))

site_navbars.register(pharmacy)
