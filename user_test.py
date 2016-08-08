import unittest
from user import *

class TestUser(unittest.TestCase):


  @classmethod
  def setUp(self):
    ''' We are setting this up as self.customer that way we do not have to
        redefine customer in every method below '''
    self.customer = User(
                        'bob',
                        '123 Main Street',
                        'Nashville',
                        'Tennessee',
                        '11111',
                        '1231231234'
                        )



  def test_customer_creation(self):
    ''' Test that a customer was created with all the prompts attributes '''
    self.assertIsInstance(self.customer, User)
    self.assertEqual(self.customer.name, 'bob')
    self.assertEqual(self.customer.address, '123 Main Street')
    self.assertEqual(self.customer.city, 'Nashville')
    self.assertEqual(self.customer.state, 'Tennessee')
    self.assertEqual(self.customer.zipcode, '11111')
    self.assertEqual(self.customer.phone, '1231231234')














if __name__ == '__main__':
    unittest.main()
