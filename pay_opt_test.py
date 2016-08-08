import unittest
from user import *
from pay_opt import *


class TestPayOption(unittest.TestCase):


  @classmethod
  def setUp(self):
    ''' We are setting this up as self.pay_opt that way we do not have to
        redefine customer in every method below '''
    self.pay_opt = Pay_Option(
                        'Visa',
                        '1234',
                        'asdf'
                        )


  def test_payment_option_creation(self):
    ''' Test that a pay option was created with all the prompts attributes '''
    self.assertIsInstance(self.pay_opt, Pay_Option)
    self.assertEqual(self.pay_opt.payment_name, 'Visa')
    self.assertEqual(self.pay_opt.account, '1234')
    self.assertEqual(self.pay_opt.cust_uid, 'asdf')





if __name__ == '__main__':
    unittest.main()
