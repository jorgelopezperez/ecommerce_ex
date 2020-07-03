import unittest

from models.cart import Cart
from models.product import Product


class Part1TestCase(unittest.TestCase):

    def test_total_product_discounts(self):
        product = Product(sku='prod-a', name='Producto A')
        product.set_pricing(country_code='ES', price=50., discount=0.)
        product.set_pricing(country_code='GB', price=55., discount=0.1)
        product.set_pricing(country_code='IT', price=55., discount=0.25)

        cart = Cart()
        cart.add_item(product=product, quantity=2)

        self.assertEqual(cart.get_total(country_code='ES'), 100.0)
        self.assertEqual(cart.get_total(country_code='GB'), 99.0)
        self.assertEqual(cart.get_total(country_code='IT'), 82.5)

    def test_total_voucher(self):
        product_a = Product(sku='prod-a', name='Producto A')
        product_a.set_pricing(country_code='ES', price=50., discount=0.1)
        product_b = Product(sku='prod-b', name='Producto B')
        product_b.set_pricing(country_code='ES', price=20., discount=0.)

        cart = Cart()
        cart.apply_voucher(code='promo5', amount=5., min_amount=90.)

        cart.add_item(product=product_a, quantity=1)
        cart.add_item(product=product_b, quantity=1)
        self.assertEqual(cart.get_total(country_code='ES'), 65.0)

        cart.add_item(product=product_a, quantity=1)
        self.assertEqual(cart.get_total(country_code='ES'), 105.0)
