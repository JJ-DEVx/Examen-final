import unittest
from backend.app import app

class APITest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_workshops(self):
        response = self.client.get('/workshops')
        self.assertEqual(response.status_code, 200)

    def test_create_workshop(self):
        response = self.client.post('/workshops', json={
            "name": "Test",
            "description": "Test desc",
            "date": "2026-01-01",
            "time": "10:00",
            "place": "Salon",
            "category": "Tech"
        })
        self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()