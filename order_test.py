import unittest
from order import *

class TestOrder(unittest.TestCase):

  @classmethod
  def setUp(self):
    ''' Set up class in order to test core functionality associated with orders'''
    self.new_order = Order(
                          'Test Cust_Uid',
                          'Test Pay_Opt_Uid',
                          paid = False
                          )

  def test_order_creation(self):
    ''' Test that an order is created with the proper attributes '''

    self.assertIsInstance(self.new_order, Order)
    self.assertEqual(self.new_order.cust_uid, 'Test Cust_Uid')
    self.assertEqual(self.new_order.pay_opt_uid, 'Test Pay_Opt_Uid')
    self.assertFalse(self.new_order.paid)


if __name__ == '__main__':
    unittest.main()