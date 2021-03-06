"""Module for user tests"""
import json
from tests.v2.test_base import ApiTestCase
from app.api_v2.models import MAIL
class UserTest(ApiTestCase):
    """Class for user tests"""
    user_data = {
        'username': 'test user',
        'email': 'test@email.com',
        'password': 'Ab123456!',
    }

    def test_registration(self):
        """Test user registration"""
        response = self.app.post('/api/v2/auth/register', data=self.user_data)
        data = json.loads(response.data.decode('utf-8'))
        self.assertDictEqual({"id":1, "username":"test user", "email":"test@email.com"}, data)
        
    def test_duplicate_registration(self):
        """Test if duplicate emails registration is not successful"""
        response = self.app.post('/api/v2/auth/register', data=self.user_data)
        data = json.loads(response.data.decode('utf-8'))
        self.assertDictEqual({"id":1, "username":"test user", "email":"test@email.com"}, data)

        response = self.app.post('/api/v2/auth/register', data=self.user_data)
        data = json.loads(response.data.decode('utf-8'))
        self.assertDictEqual({"success": False, "message": "email already in exists in the system"}, data)

    def test_user_login(self):
        """Test user login"""
        response = self.app.post('/api/v2/auth/register', data=self.user_data)
        data = json.loads(response.data.decode('utf-8'))
        self.assertDictEqual({"id":1, "username":"test user", "email":"test@email.com"}, data)

        response = self.app.post('/api/v2/auth/login', data=self.user_data)
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue(data.get('success'))
    def test_user_logout(self):
        """Test user logout"""
        response = self.app.post('/api/v2/auth/register', data=self.user_data)
        data = json.loads(response.data.decode('utf-8'))
        self.assertDictEqual({"id":1, "username":"test user", "email":"test@email.com"}, data)

        response = self.app.post('/api/v2/auth/login', data=self.user_data)
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue(data.get('success'))

        token = data.get('payload').get('token')
        response = self.app.post('api/v2/auth/logout', data=self.user_data, headers={'Authorization':' Bearer '+token})
        self.assertTrue(data.get('success'))
    def test_password_reset(self):
        """test if users can successfully reset their passwords"""
        response = self.app.post('/api/v2/auth/register', data={
            'username': 'test user',
            'email': 'paulrimiru@gmail.com',
            'password': 'Ab123456!',
        })
        data = json.loads(response.data.decode('utf-8'))
        self.assertDictEqual({"id":1, "username":"test user", "email":"paulrimiru@gmail.com"}, data)

        response = self.app.put('/api/v2/auth/reset-password', data={
            'code': "bad code",
            'password': 'Aabc123!'
        })
        
        data = json.loads(response.data.decode('utf-8'))
        self.assertFalse(data.get('success'))

