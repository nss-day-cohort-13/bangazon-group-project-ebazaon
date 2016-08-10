import uuid


class LineItems:
  ''' Creates a new lineItem with the following attributes passed in below in the __init__ method
      line 10 creates a unique id for each lineItem created '''
  def __init__(self, productID, orderID):
    self.productID = productID
    self.orderID = orderID



