import uuid

class Order:
  ''' Creates an order containing unique IDs for customer and payment option as well as holds a boolean value indicating whether or not an order has been paid (defaults to false aka unpaid) '''
  def __init__(self, cust_uid, pay_opt_uid, paid = False):
    self.cust_uid = cust_uid
    self.pay_opt_uid = pay_opt_uid
    self.paid = paid
    self.order_uuid = uuid.uuid4()