import pickle

# ----- Serialization of all users -------#

def serialize_users():
  with open('users.txt', 'wb+') as f:
    pickle.dump(all_users, f)


def deserialize_users():
  try:
    with open('users.txt', 'rb+') as f:
      all_users = pickle.load(f)

  except EOFError:
    pass




# ----- Serialization of all payment options -------#

def serialize_pay_opt():
  with open('pay_opt.txt', 'wb+') as f:
    pickle.dump(all_pay_opt, f)


def deserialize_pay_opt():
  try:
    with open('pay_opt.txt', 'rb+') as f:
      all_pay_opt = pickle.load(f)

  except EOFError:
    pass




# ----- Serialization of all products -------#

def serialize_products():
  with open('products.txt', 'wb+') as f:
    pickle.dump(all_products, f)


def deserialize_products():
  try:
    with open('products.txt', 'rb+') as f:
      all_products = pickle.load(f)

  except EOFError:
    pass




# ----- Serialization of all orders -------#

def serialize_orders():
  with open('orders.txt', 'wb+') as f:
    pickle.dump(all_orders, f)


def deserialize_orders():
  try:
    with open('orders.txt', 'rb+') as f:
      all_orders = pickle.load(f)

  except EOFError:
    pass




# ----- Serialization of all order_line_items -------#

def serialize_order_line_itmes():
  with open('order_line_items.txt', 'wb+') as f:
    pickle.dump(all_order_line_items, f)


def deserialize_order_line_items():
  try:
    with open('order_line_items.txt', 'rb+') as f:
      all_order_line_items = pickle.load(f)

  except EOFError:
    pass
