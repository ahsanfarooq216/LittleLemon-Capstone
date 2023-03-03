from django.test import TestCase
from .models import MenuItem

# class menuItemTest(TestCase):
#     def test_get_item(self):
#         item = menuItem.objects.create(title="IceCream", price=8.95, inventory=100)
#         self.assertEqual(str(item), "IceCream : 8.95")

class MenuTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        MenuItem.objects.create(title="IceCream", price=8.95, inventory=100)

    def  test_get_item(self):
        menuItem = MenuItem.objects.get(id=1)
        self.assertEqual(str(menuItem), "IceCream : 8.95")
        
    def test_title_label(self):
        menuItem = MenuItem.objects.get(id=1)
        field_label = menuItem._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
    def test_price_label(self):
        menuItem = MenuItem.objects.get(id=1)
        field_label = menuItem._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_inventory_label(self):
        menuItem = MenuItem.objects.get(id=1)
        field_label = menuItem._meta.get_field('inventory').verbose_name
        self.assertEqual(field_label, 'inventory')

    def test_title_max_length(self):
        menuItem = MenuItem.objects.get(id=1)
        max_length = menuItem._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_item_title_and_price(self):
        menuItem = MenuItem.objects.get(id=1)
        expected_object_name = f'{menuItem.title} : {str(menuItem.price)}'
        self.assertEqual(expected_object_name, str(menuItem))