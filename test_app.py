import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "¡Hola, CI/CD con GitHub Actions!"})

if __name__ == "__main__":
    unittest.main()
