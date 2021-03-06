import unittest
import requests
import json
from app import APP
class TestViews(unittest.TestCase):
    
    def setUp(self):
        self.app = APP.test_client()
        self.user_data = {
            'email': 'user@bright.com',
            'password': 'pass123',
            'username':'test user'
            }
        self.login_data = {
            'email': 'user@bright.com',
            'password': 'pass123'
        }
        self.event_data = {
            'name':'test event',
            'location':'Nairobi',
            'time':'5/6/2016',
            'creator':1,
            'category':'private',
            'rsvp':[]
        }
        self.event_data2 = {
            'name':'test event',
            'location':'Nairobi',
            'time':'5/6/2016',
            'creator':1,
            'category':'public',
            'rsvp':[]
        }

    def test_register(self):
        resp = self.app.post('/api/v1/auth/register', data=self.user_data)
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.post('/api/v1/auth/login', data=self.login_data)
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.post('/api/v1/auth/logout', data={'id':1})
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.post('/api/v1/auth/reset-password', data={
            'email': 'user@bright.com',
            'password': 'pass1231234'
        })

        resp = self.app.post('/api/v1/auth/login', data={
            'email': 'user@bright.com',
            'password': 'pass1231234'
        })
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.post('/api/v1/events', data=self.event_data)
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.get('/api/v1/events', data=self.event_data)
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.delete('/api/v1/events/11', data=self.event_data)
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.post('/api/v1/events', data=self.event_data)
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.post("/api/v1/event/10/rsvp", data={'creator':'1','client_email':'myemail@gmail.com'})
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.get("/api/v1/event/10/rsvp", data={'client_email':'1'})
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.put("/api/v1/manageRsvp", data={'event_id':'10', 'action':'accept', 'client_email':'myemail@gmail.com'})
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.put("/api/v1/manageRsvp", data={'event_id':'10', 'action':'reject', 'client_email':'myemail@gmail.com'})
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        resp = self.app.put('/api/v1/events/10', data=self.event_data2)
        data = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

