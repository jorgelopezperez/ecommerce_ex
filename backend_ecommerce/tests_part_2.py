import unittest

from models.cart import Cart
from models.product import Product


class Part2TestCase(unittest.TestCase):

    def test_quantity_discount(self):
        product_a = Product(sku='prod-a', name='Producto A')
        product_a.set_pricing(
            country_code='ES', price=50., discount=0.1,
            quantity_discount=[
                {'min_quantity': 3, 'discount': 45., 'is_percent': False}
            ]
        )
        product_b = Product(sku='prod-b', name='Producto B')
        product_b.set_pricing(
            country_code='ES', price=1.5, discount=0.,
            quantity_discount=[
                {'min_quantity': 10, 'discount': 5., 'is_percent': False},
                {'min_quantity': 50, 'discount': 0.1, 'is_percent': True},
                {'min_quantity': 200, 'discount': 0.2, 'is_percent': True}
            ]
        )

        cart = Cart()
        cart.apply_voucher(code='promo100', amount=100., min_amount=200.)

        cart.add_item(product=product_a, quantity=1)
        cart.add_item(product=product_b, quantity=1)
        self.assertEqual(cart.get_total(country_code='ES'), 46.5)

        cart.add_item(product=product_a, quantity=2)
        cart.add_item(product=product_b, quantity=8)
        self.assertEqual(cart.get_total(country_code='ES'), 103.5)

        cart.add_item(product=product_b, quantity=1)
        self.assertEqual(cart.get_total(country_code='ES'), 100.0)

        cart.add_item(product=product_b, quantity=50)
        self.assertEqual(cart.get_total(country_code='ES'), 171.0)

        cart.add_item(product=product_a, quantity=1)
        cart.add_item(product=product_b, quantity=50)
        self.assertEqual(cart.get_total(country_code='ES'), 183.5)

        cart.add_item(product=product_a, quantity=2)
        cart.add_item(product=product_b, quantity=90)
        self.assertEqual(cart.get_total(country_code='ES'), 365.0)
