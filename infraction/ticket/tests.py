from django.test import TestCase
from django.test.client import Client

class TicketTest(TestCase):
    def test_get_ticket_by_email(self):
        response = self.client.get('/generar_informe?email=wzunigah@gmail.com')
        self.assertEqual(response.status_code, 200)
    
    def test_get_ticket_by_email_no_exist_email(self):
        response = self.client.get('/generar_informe?email=wzuniga@gmail.com')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('[]' in str(response.content))
