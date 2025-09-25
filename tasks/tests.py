from rest_framework.test import APITestCase

class TaskTests(APITestCase):
    def setUp(self):
        self.client.post("/api/accounts/register/", {"username": "u", "password": "p"})
        token = self.client.post("/api/accounts/login/", {"username": "u", "password": "p"}).data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_create_tasks(self):
        res = self.client.post("/api/tasks/", {"title": "Adv Alg", "due_date": "2025-09-25"})
        self.assertEqual(res.status_code, 201)

        res = self.client.get("/api/tasks/")
        self.assertEqual(res.data, [{'id': 1, 'title': 'Adv Alg', 'due_date': '2025-09-25'}])
