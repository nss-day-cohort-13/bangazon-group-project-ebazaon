import uuid

class User:
  ''' Creates a user with the following attributes passed in below in the __init__ method
      line 14 creates a unique id for each customer created '''
  def __init__(self, name, address, city, state, zipcode, phone):
    self.name = name
    self.address = address
    self.city = city
    self.state = state
    self.zipcode = zipcode
    self.phone = phone






