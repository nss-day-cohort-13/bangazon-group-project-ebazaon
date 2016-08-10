import pickle
from menu import *


def serializeUser(self):
  with open('users.txt', 'wb+') as u:
    pickle.dump(self.userDict, u)

def deserializeUser(self):
  try:
    with open('users.txt', 'rb+') as u: #rb in read binary
      self.userDict = pickle.load(u)

  except EOFError:
    self.userDict = {}

  except FileNotFoundError:
    self.userDict = {}






def serializePayment(self):
  with open('pay_opt.txt', 'wb+') as u:
    pickle.dump(self.paymentDict, u)

def deserializePayment(self):
  try:
    with open('pay_opt.txt', 'rb+') as u: #rb in read binary
      self.paymentDict = pickle.load(u)

  except EOFError:
    self.paymentDict = {}

  except FileNotFoundError:
    self.paymentDict = {}






def serializeProduct(self):
  with open('products.txt', 'wb+') as u:
    pickle.dump(self.ProductDict, u)

def deserializeProduct(self):
  try:
    with open('products.txt', 'rb+') as u: #rb in read binary
      self.productDict = pickle.load(u)

  except EOFError:
    self.productDict = {}

  except FileNotFoundError:
    self.productDict = {}






def serializeOrders(self):
  with open('orders.txt', 'wb+') as u:
    pickle.dump(self.ordersDict, u)

def deserializeOrders(self):
  try:
    with open('orders.txt', 'rb+') as u: #rb in read binary
      self.ordersDict = pickle.load(u)

  except EOFError:
    self.ordersDict = {}

  except FileNotFoundError:
    self.ordersDict = {}






def serializeLineItems(self):
  with open('order_line_items.txt', 'wb+') as u:
    pickle.dump(self.lineItemsDict, u)

def deserializeLineItems(self):
  try:
    with open('order_line_items.txt', 'rb+') as u: #rb in read binary
      self.lineItemsDict = pickle.load(u)

  except EOFError:
    self.lineItemsDict = {}

  except FileNotFoundError:
    self.lineItemsDict = {}
