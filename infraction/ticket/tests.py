from django.test import TestCase
from django.test.client import Client
import base64
import requests
import json

client_id = "TbOOwfsPDJPApZnbmyH2CYNktykfvhiroqX806f5"
client_secret = "b8v582JhXbYQ72ieCSALyxj9vqiNPWsb8RdFVvZUXSDUx72uXg6jt2omOMBDQxQVsudgvldPg05jwhlvmeSjE8MdGJOud92waxIsHuo7UZwsSOmHcSrCuWpEzrER02gZ"

def get_basic_token(client_id, client_secret):
    credential = "{0}:{1}".format(client_id, client_secret)
    basic_token_bas64 = base64.b64encode(credential.encode("utf-8"))
    basic_token = basic_token_bas64.decode("utf-8")
    return basic_token

def get_token_bearer(url, basic_token):
    payload='grant_type=client_credentials'
    headers = {
        'Authorization': 'Basic ' + basic_token,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response

class TicketTest(TestCase):
    def test_get_ticket_by_email(self):
        response = self.client.get('/generar_informe?email=wzunigah@gmail.com')

        self.assertEqual(response.status_code, 200)
    
    def test_get_ticket_by_email_no_exist_email(self):
        response = self.client.get('/generar_informe?email=no_exist@gmail.com')

        self.assertEqual(response.status_code, 200)
        self.assertTrue('[]' in str(response.content))

    def test_token_bearer_creation(self):
        basic_token = get_basic_token(client_id, client_secret)
        url = "http://localhost:8000/o/token/"
        response = get_token_bearer(url, basic_token)
        
        self.assertEqual(response.status_code, 200)

    def test_post_create_ticket_successfully(self):
        basic_token = get_basic_token(client_id, client_secret)
        url_token = "http://localhost:8000/o/token/"
        response = get_token_bearer(url_token, basic_token)
        access_token = response.json()["access_token"]

        url_upload_infraction = "http://localhost:8000/cargar_infraccion?access_token=" + access_token
        
        payload = json.dumps({
            "placa_patente": "z50251",
            "timestamp": 1676781429,
            "comentarios": "Commentario 3"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url_upload_infraction, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "ticket created successfully!")
        
    def test_post_create_ticket_content_body_invalid(self):
        basic_token = get_basic_token(client_id, client_secret)
        url_token = "http://localhost:8000/o/token/"
        response = get_token_bearer(url_token, basic_token)
        access_token = response.json()["access_token"]

        url_upload_infraction = "http://localhost:8000/cargar_infraccion?access_token=" + access_token
        
        payload = {
            "placa_patente": "z50251",
            "timestamp": 1676781429,
            "comentarios": "Commentario 3"
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url_upload_infraction, headers=headers, data=payload)

        self.assertEqual(response.status_code, 500)

    def test_post_create_ticket_plate_invalid(self):
        basic_token = get_basic_token(client_id, client_secret)
        url_token = "http://localhost:8000/o/token/"
        response = get_token_bearer(url_token, basic_token)
        access_token = response.json()["access_token"]

        url_upload_infraction = "http://localhost:8000/cargar_infraccion?access_token=" + access_token
        
        payload = {
            "placa_patente": "000000",
            "timestamp": 1676781429,
            "comentarios": "Commentario 3"
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url_upload_infraction, headers=headers, data=payload)

        self.assertEqual(response.status_code, 500)
