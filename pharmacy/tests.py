from django.contrib.admin.sites import all_sites
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from pprint import pprint


class TestMe(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username='jacob', email='jacob@…', password='top_secret')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/')
        request.user = self.user
        for site in all_sites:
            try:
                print(site.name, reverse(f'{site.name}:index'))
            except NoReverseMatch:
                pass
            else:
                pprint(site.__dict__)
