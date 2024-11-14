from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuTest(TestCase):
    def test_menu(self):
        menu = Menu.objects.create(title='Fried Rice',price=8.50,inventory=50)
        self.assertEqual(str(menu),'Fried Rice')