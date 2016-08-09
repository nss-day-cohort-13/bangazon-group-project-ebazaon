import unittest
from user import *
from pay_opt import *
from product import *


class TestProduct(unittest.TestCase):

  @classmethod
  def setUp(self):
    ''' We are setting this up as self.product that way we do not have to
        redefine product in every method below '''
    self.product = Product(
                        'milk',
                        '2.00'
                        )


  def test_product_object_creation(self):
    self.assertIsInstance(self.product, Product)
    self.assertEqual(self.product.name, 'milk')
    self.assertEqual(self.product.price, '2.00')


if __name__ == '__main__':
    unittest.main()
