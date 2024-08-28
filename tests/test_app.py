import unittest
from app import create_app

class FlaskAppTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Create the Flask application instance for testing
        cls.app = create_app()
        cls.client = cls.app.test_client()
        cls.app.testing = True

    def test_home_page(self):
        # Test the home page route
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to My Web App!', response.data)

    def test_about_endpoint(self):
        # Test the /about endpoint
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About BBT Lab App01', response.data)

    def test_contact_endpoint(self):
        # Test the /about endpoint
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact Us', response.data)

    def test_404_error(self):
        # Test that a non-existent route returns a 404 error
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'404 Not Found', response.data)

if __name__ == '__main__':
    unittest.main()
