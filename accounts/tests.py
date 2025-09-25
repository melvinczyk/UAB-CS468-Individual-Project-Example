from rest_framework.test import APITestCase

class AuthTests(APITestCase):
    def test_register_and_login(self):
        res = self.client.post("/api/accounts/register/", {"username": "a", "password": "p"})
        self.assertEqual(res.status_code, 201)

        res = self.client.post("/api/accounts/login/", {"username": "a", "password": "p"})
        self.assertIn("access", res.data)
