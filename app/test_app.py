
import unittest
from app import app


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_homepage_returns_success(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_contains_hello_message(self):
        response = self.client.get("/")
        self.assertIn(b"Hello from DevOps!", response.data)


if __name__ == "__main__":
    unittest.main()
