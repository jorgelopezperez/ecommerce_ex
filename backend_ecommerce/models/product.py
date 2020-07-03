#!/usr/bin/python
# -*- encoding: utf-8 -*-
################################################################################
#    Date: 02/07/2020
#    Copyright (C) 2020 Jorge López Pérez <jorgelopez.physics@gmail.com>.
#    Licence : BSD, see LICENSE for more details.
#
################################################################################


class Product:
    """
    Class to describe Product in a e-commerce site.
    A Product instance can contain several values for (country_code, price, discount)
    The class variable price_result_ctr will be a unnormalized (flatten) objects in the form of list of dicts
    with all information: name, slug (sku), country_code, price, discount, quantity_discount, final_price
    """

    product_info = {}
    product_info_ = {}
    price_result_ctr = []
    tramos = {}

    def __init__(self, name, sku, price_result_ctr=None, discount_list={}):
        """
        :param name: Name for the instance of :class:`Product`.
        :param sku: slug-like for the instance of :class:`Product`.
        :param price_result_ctr: Product price(default {}).
        After inserting data, this will be a list of dicts with the following fields:
            "slug": "prod-a,
            "country_code": "ES",
            "price": 55,
            "discount": 0.1,
            "quantity_discount": [{'min_quantity': 3, 'discount': 45., 'is_percent': False}],
            "final_price": price * (1 - discount),
        """
        self.name = name
        self.sku = sku
        self._tramo_descuento = False
        if price_result_ctr is None:
            self.price_result_ctr = []
        else:
            self.price_result_ctr = price_result_ctr

    def __repr__(self):
        return f"{self.__class__.__name__}" f"(rank={self.name!r}, suit={self.sku!r})"

    def set_pricing(self, country_code, price, discount, quantity_discount=None):
        """
        To set pricing with a declared discount to Product instance
        :param country_code: Country code for the product
        :param price: Price for the product.
        :param discount: Discount for the product.
        :param quantity_discount: If flow of discount is applied to a Product (default None).
        """
        if quantity_discount is not None:
            self._tramo_descuento = True
            self.discount_list = quantity_discount
            self.tramos = {"slug": self.sku, "tramos": quantity_discount}
        self.price_result_ctr.extend(
            [
                {
                    "slug": self.sku,
                    "country_code": country_code,
                    "price": price,
                    "discount": discount,
                    "quantity_discount": quantity_discount,
                    "final_price": price * (1 - discount),
                }
            ]
        )

    def has_discount_tramo(self):
        return True if self._tramo_descuento is True else False
