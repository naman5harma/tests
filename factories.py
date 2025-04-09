# tests/factories.py

import random
import string

class Product:
    def __init__(self, name, description, price, sku, in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.sku = sku
        self.in_stock = in_stock

    def __repr__(self):
        return f"<Product name={self.name}, price={self.price}, sku={self.sku}, in_stock={self.in_stock}>"

class ProductFactory:
    @staticmethod
    def create():
        name = ProductFactory._random_word().capitalize()
        description = ProductFactory._random_sentence()
        price = round(random.uniform(5.0, 999.99), 2)
        sku = ProductFactory._random_sku()
        in_stock = random.choice([True, False])
        return Product(name, description, price, sku, in_stock)

    @staticmethod
    def _random_word(length=8):
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    @staticmethod
    def _random_sentence(word_count=10):
        return ' '.join(ProductFactory._random_word(random.randint(4, 10)) for _ in range(word_count)).capitalize() + '.'

    @staticmethod
    def _random_sku(length=13):
        return ''.join(random.choices(string.digits, k=length))
