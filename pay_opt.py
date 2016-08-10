import uuid
from user import *


class Pay_Option:
  ''' Creates a user with the following attributes passed in below in the __init__ method
      line 14 creates a unique id for each customer created '''
  def __init__(self, payment_name, account): #cust_uid as 3rd argument
    self.payment_name = payment_name
    self.account = account
    # self.cust_uid = cust_uid

