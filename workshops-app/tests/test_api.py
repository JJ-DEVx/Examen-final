import unittest
from backend.app import app

class APITest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_workshops(self):
        response = self.client.get('/workshops')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()