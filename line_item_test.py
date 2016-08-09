import unittest
from line_item import *

class TestLineItems(unittest.TestCase):


  @classmethod
  def setUp(self):
    ''' We are setting this up as self.lineItem that way we do not have to
        redefine lineItem in every method below '''
    self.lineItem = LineItems(
                        '93595a49-4462-473d-8aea-75c0e81bb4c6',
                        '13595a49-4462-473d-8aea-75c0e81bb4c6'
                        )



  def test_lineItem_creation(self):
    ''' Test that a lineItem was created with all the prompts attributes '''
    self.assertIsInstance(self.lineItem, LineItems)
    self.assertEqual(self.lineItem.productID, '93595a49-4462-473d-8aea-75c0e81bb4c6')
    self.assertEqual(self.lineItem.orderID, '13595a49-4462-473d-8aea-75c0e81bb4c6')




if __name__ == '__main__':
    unittest.main()
