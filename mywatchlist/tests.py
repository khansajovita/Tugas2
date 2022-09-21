from urllib import response
from django.test import TestCase, Client

# Create your tests here.
class TestMywatchlist(TestCase):
    def testing_html(self):
        response = Client().get('/mywatchlist/html')
        self.assertEqual(response.status_code, 200)

    def testing_xml(self):
        response = Client().get('/mywatchlist/xml')
        self.assertEqual(response.status_code, 200)
        
    def testing_json(self):
        response = Client().get('/mywatchlist/json')
        self.assertEqual(response.status_code, 200)

