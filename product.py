import uuid


class Product:
  ''' Creates a user with the following attributes passed in below in the __init__ method
      line 14 creates a unique id for each customer created '''
  def __init__(self, product_name, product_price):
    self.name = product_name
    self.price = product_price

