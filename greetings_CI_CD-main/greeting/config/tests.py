from django.test import TestCase, Client
from django.urls import reverse

class GreetingViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello')
        self.assertTemplateUsed(response, 'index.html')
        
    def test_404_page(self):
        response = self.client.get('/nonexistent-url/')
        self.assertEqual(response.status_code, 404)

    def test_wrong_template(self):
        response = self.client.get(reverse('wrong'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'index.html')


