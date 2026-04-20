<<<<<<< HEAD
import unittest
from backend.app import app

class APITest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_workshops(self):
        response = self.client.get('/workshops')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
=======
import unittest
from backend.app import app

class APITest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_workshops(self):
        response = self.client.get('/workshops')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
>>>>>>> 56e814f15d8c66ed8a42f98983505eb945d62847
    unittest.main()