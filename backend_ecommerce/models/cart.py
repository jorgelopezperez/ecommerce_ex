#!/usr/bin/python
# -*- encoding: utf-8 -*-
################################################################################
#    Date: 02/07/2020
#    Copyright (C) 2020 Jorge López Pérez <jorgelopez.physics@gmail.com>.
#    Licence : BSD, see LICENSE for more details.
#
################################################################################

from .utils import transform_tramo_discount


class Cart:
    """
        Class to describe a shopping Cart in a e-commerce site
        A Cart instance can contain several products
    """

    products_in_cart = []
    tramos = []
    voucher_info = {}

    def __init__(self, products_in_cart=None):
        self._voucher = False
        if products_in_cart is None:
            self.products_in_cart = []

    def add_item(self, product, quantity):
        """
        :param product: Instance of :class:`Product`.
        :param quantity: Number of products inside that cart
        product.price_result_ctr can be a list of dicts for a given product instance
        if several countries has been assigned
        """
        self.products_in_cart.extend(product.price_result_ctr * quantity)

    def get_products_in_cart(self):
        """
        This instance method returns a tuple with number of different product instances and the sku ("slug") for each
        """
        return (
            len(set([el["slug"] for el in self.products_in_cart])),
            list(set([el["slug"] for el in self.products_in_cart])),
        )

    def get_list_by_product(self, slug_name):
        """
        This instance method filters the flatten list dict by sku ("slug") field
        """
        return [el for el in self.products_in_cart if el["slug"] == slug_name]

    def get_tramos_by_product(self, slug_name):
        """
        This instance method filters the flatten list dict by quantity_discount field
        """
        return [
            el["quantity_discount"]
            for el in self.products_in_cart
            if el["slug"] == slug_name
        ][0]

    def apply_voucher(self, code, amount, min_amount):
        """
        This instance method apply a voucher to the Cart instance
        """
        self._voucher = True
        self.voucher_info = {"amount": amount, "min_amount": min_amount}

    def has_voucher(self):
        return True if self._voucher is True else False

    def _get_tramo_discount(self, tramo, quant):
        """
        :param tramo: This is a list of dict in this way [{'min_quantity': 3, 'discount': 45.0, 'is_percent': False}]
        :param quant: This is an integer
        :return: index of dict telling the range in prices in which discount is applied.
        For instance, if quant is 12
        and tramo is [{'min_quantity': 10, 'discount': 5.0, 'is_percent': False}, {'min_quantity': 50, 'discount': 0.1,
        'is_percent': True}, {'min_quantity': 200, 'discount': 0.2, 'is_percent': True}]
        index will be 1 because it ranges quantities between 11 and 49
		"""
        if not isinstance(tramo, list):
            raise TypeError('tramo field value must be a list', 'tramo')
        if not isinstance(quant, int):
            raise TypeError('quant field value must be a integer', 'tramo')
        num_tram_instance = len([el["min_quantity"] for el in tramo])

        ranges = transform_tramo_discount([el["min_quantity"] for el in tramo])
        if not any(quant in el for el in ranges):
            # All are False in the boolean list
            return None
        else:
            idx_detected = [i for i, x in enumerate(quant in el for el in ranges) if x][
                0
            ]
            return idx_detected

    def get_total(self, country_code):
        """
        :param country_code: Country code to get total price for all products in a cart
        To compute the total price for a given country, a filter in a list of dicts (get_products_in_cart method on
        cart instance) is carried out. This list of dicts will contain either:
         - a single product for different countries
         or:
         - different products with different countries for each
        """
        num_prods, prods = self.get_products_in_cart()
        total_price = 0
        for pr in prods:
            # prod-a, prod-b
            # get tramo for a product in the cart
            tramos = self.get_tramos_by_product(pr)
            if not tramos:
                # No tramo
                total_price += sum(
                    [
                        el["final_price"]
                        for el in self.products_in_cart
                        if el["country_code"] == country_code and el["slug"] == pr
                    ]
                )
            else:
                # Si hay tramo
                quant = len(
                    [
                        el
                        for el in self.products_in_cart
                        if el["country_code"] == country_code and el["slug"] == pr
                    ]
                )
                tmp = self._get_tramo_discount(tramos, quant)
                if tmp is None:
                    # Hay tramo pero para esta quant no se aplica
                    total_price += sum(
                        [
                            el["final_price"]
                            for el in self.products_in_cart
                            if el["country_code"] == country_code and el["slug"] == pr
                        ]
                    )
                else:
                    # Hay tramo Y sí que se aplica para esta quant
                    if tramos[tmp]["is_percent"] == False:
                        # No percent. Just drop for final quantity
                        total_price += (
                                sum(
                                    [
                                        el["final_price"]
                                        for el in self.products_in_cart
                                        if el["country_code"] == country_code
                                           and el["slug"] == pr
                                    ]
                                )
                                - tramos[tmp]["discount"]
                        )
                    else:
                        # Is percent. Make adjustment with price(1-discount_in_percent)
                        # print(tramos[tmp]["discount"])
                        total_price += sum(
                            [
                                el["final_price"]
                                for el in self.products_in_cart
                                if el["country_code"] == country_code
                                   and el["slug"] == pr
                            ]
                        ) * (1 - tramos[tmp]["discount"])

            # print("total price for product")
            # print(pr, total_price)

        if not self._voucher:
            pass
        else:
            if total_price >= self.voucher_info["min_amount"]:
                total_price = total_price - self.voucher_info["amount"]
            else:
                pass

        return total_price

    def clear_data(self):
        self.products_in_cart = []
