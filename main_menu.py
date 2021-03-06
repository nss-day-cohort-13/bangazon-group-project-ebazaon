import os
import sys
import sqlite3
from user import *
from pay_opt import *
from orders import *
from line_item import *
from products import *
# import serialization

# all_users = {}
# all_pay_opt = {}
# all_products = {}
# all_orders = {}
# all_order_line_items = {}

menu_display = True
menu_error = False
menu_not_num = False
user_login = False
current_user = None
current_order = None

def app_start():

    # Verify is working
    # global all_users
    # all_users = serialization.deserialize_users() #this will contain the entire dict of all users

    # global all_pay_opt
    # all_pay_opt = serialization.deserialize_pay_opt() #this will contain the entire dict of all pay options

    # global all_products
    # all_products = serialization.deserialize_products() #this will contain the entire dict of all users

    # global all_orders
    # all_orders = serialization.deserialize_orders() #this will contain the entire dict of all users

    # global all_order_line_items
    # all_order_line_items = serialization.deserialize_order_line_items() #this will contain the entire dict of all users

    start_menu()


def start_menu():

    global menu_display
    while menu_display == True:
      os.system('cls' if os.name == 'nt' else 'clear')

      print(current_user)

      print("*********************************************************")
      print("**  Welcome to Ebazaon! Command Line Ordering System!  **")
      print("*********************************************************")

      global user_login
      if user_login == True:
        print("\n")
        global current_user
        print("Welcome {}!".format(current_user.name))
        print("\n")

      print("1. Create a customer account")
      print("2. Choose active customer")
      print("3. Create a payment option")
      print("4. Add product to shopping cart")
      print("5. Complete an order")
      print("6. See product popularity")
      print("7. Leave Ebazaon!")
      print("\n")

      global menu_error
      if menu_error == True:
        menu_error = False
        print("Please choose a number within option range")

      global menu_not_num
      if menu_not_num == True:
        menu_not_num = False
        print("Please choose a number to indicate your selection")

      menu_selection = input("> ")
      route_user_selection(menu_selection)


def route_user_selection(selection):

  try:
    if int(selection) == 0:
      admin_menu()
    elif int(selection) == 1:
      create_customer_menu()
    elif int(selection) == 2:
      choose_customer_menu()
    elif int(selection) == 3:
      create_pay_opt_menu()
    elif int(selection) == 4:
      add_product_menu()
    elif int(selection) == 5:
      complete_order_menu()
    elif int(selection) == 6:
      see_popularity_menu()
    elif int(selection) == 7:
      leave_ebazaon()
    else:
      global menu_error
      menu_error = True
      return("invalid selection")
  except ValueError:
      global menu_not_num
      menu_not_num = True
      return("invalid selection")


def create_customer_menu():

  global current_user
  global menu_display
  global all_users
  menu_display = False

  print(current_user)

  os.system('cls' if os.name == 'nt' else 'clear')

  with sqlite3.connect('bangazon.db') as conn:
    c = conn.cursor()

    print("Enter customer name")
    name = input("> ")

    print("Enter street address")
    address = input("> ")

    print("Enter city")
    city = input("> ")

    print("Enter state")
    state = input("> ")

    print("Enter postal code")
    zipcode = input("> ")

    # print("Enter phone number")
    # phone = input("> ")

    c.execute("""
                insert into Customer (FullName, Address, City, StateOfResidence, ZipCode)
                values (?, ?, ?, ?, ?)
              """,
                (name, address, city, state, zipcode))
    conn.commit()


    c.execute("""
                SELECT CustomerID
                FROM Customer
                WHERE FullName =?
                and Address =?
                and City =?
                and StateofResidence =?
                and ZipCode =?
              """,
                (name, address, city, state, zipcode))

    # print(c.fetchone())
    current_user = c.fetchone()[0]

    print(current_user)

    blah = input('dlbvlkdvbldkvbdlkv')



  # Verify is working
  # user = User(name, address, city, state, zipcode, phone)
  # all_users[user.uuid.__str__()] = user #make this an add users function then serialize it
  # print(all_users)
  # serialization.serialize_users(all_users)
  # will call function for instantiating new user, to be added later

  cust_create_success(name)

def cust_create_success(name):

  os.system('cls' if os.name == 'nt' else 'clear')

  print("We successfully added {} as a user.\n Press enter to continue.".format(name))
  print("\n")
  input("> ")
  global menu_display
  menu_display = True
  start_menu()


def choose_customer_menu():
  global current_user

  with sqlite3.connect('bangazon.db') as conn:
    c = conn.cursor()

    # query to return a list of tuples containing the Customers uid and fullname
    c.execute("""
                select
                  CustomerID,
                  FullName
                from Customer
              """)
    all_users_list = c.fetchall()

  # loop over an enumerated list of tuples to print the users with a value/number to be selected
  list_of_users = enumerate(all_users_list, start=1)
  for index, user_name in list_of_users:
    print('User: ', index, user_name[1])

  customer_selection = input('Customer number: > ')
  list_of_users = enumerate(all_users_list, start=1)
  for index, user_name in list_of_users:
    if int(customer_selection) == index:
      current_user = user_name[0] #current_user is the uid of the customer
      print(current_user)
      lol = input('imlolin')

  # menu_display = False
  # os.system('cls' if os.name == 'nt' else 'clear')
  # print("Which customer will be active?")
  # print("\n")

  # temp_user_thing = dict()
  # global all_users
  # counter = 1
  # for key, value in all_users.items():
  #   print("{}. {}".format(counter, value.name))
  #   temp_user_thing[counter] = value
  #   counter += 1

  # # need to write statement to handle exceptions
  # user_choice = int(input("> "))
  # for key, value in temp_user_thing.items():
  #   if key == user_choice:
  #     global user_login
  #     user_login = True
  #     global current_user
  #     current_user = value

  # start_menu()

    # needs to call the function that pulls the rest of the customer information

def create_pay_opt_menu():
  global current_user
  os.system('cls' if os.name == 'nt' else 'clear')

  print(current_user)

  with sqlite3.connect('bangazon.db') as conn:
    c = conn.cursor()

    print("Enter payment type (e.g. AmEx, Visa, Checking)")
    pay_type = input("> ")

    print("Enter account number")
    account = input("> ")

    c.execute("""
                insert into PaymentOption (AccountNumber, Name, CustomerID)
                values (?, ?, ?)
              """,
                (account, pay_type, current_user))
    conn.commit()

  # needs to run function to have user payment information added to file that holds that information
  # added_pay_opt_success(pay_type)

def added_pay_opt_success(pay_type):
  os.system('cls' if os.name == 'nt' else 'clear')

  print("We successfully added {} as payment method. Press enter to continue.".format(pay_type))
  print("\n")
  input("> ")
  global menu_display
  menu_display = True
  start_menu()

def add_product_menu():
  print('Add some products!')

  with sqlite3.connect('bangazon.db') as conn:
    c = conn.cursor()

    # query to return a list of tuples containing the Customers uid and fullname
    c.execute("""
                select
                  ProductName,
                  ProductPrice
                from Product
              """)
    all_products_list = c.fetchall()

  #  loop over an enumerated list of tuples to print the products with a value/number to be selected
  list_of_products = enumerate(all_products_list, start=1)
  for index, products in list_of_products:
    print('#', index, products[0], '-', products[1] )

  lol = input(">>>>>>> ")

  # for index, user_name in list_of_users:
  #   print('User: ', index, user_name[1])

  # customer_selection = input('Customer number: > ')
  # list_of_users = enumerate(all_users_list, start=1)
  # for index, user_name in list_of_users:
  #   if int(customer_selection) == index:
  #     current_user = user_name[0] #current_user is the uid of the customer
  #     print(current_user)
  #     lol = input('imlolin')

  # print("please enter as many products as you need!")
  # global all_orders
  # global all_products
  # global current_order
  # global current_user

  # if current_order:
  #   pass
  # else:
  #   current_order = Order(current_user.uuid, None)
  #   all_orders[current_order.order_uuid.__str__()] = current_order
  #   # print(all_orders)
  #   serialization.serialize_orders(all_orders)

  # done_shopping = False

  # while done_shopping == False:
  #   os.system('cls' if os.name == 'nt' else 'clear')
  #   temp_product_thing = dict()
  #   global all_products
  #   counter = 1
  #   for key, value in all_products.items():
  #     print("{}. {} - ${}".format(counter, value['name'], value['price']))
  #     temp_product_thing[counter] = value
  #     counter += 1
  #   print('{}.done'.format(counter))

  #   print('Select a product by its corresponding number:')
  #   product_choice = int(input("> "))

  #   if product_choice == counter:
  #     done_shopping = True

def complete_order_menu():
  pass
  # os.system('cls' if os.name == 'nt' else 'clear')
  print("completing order")

def see_popularity_menu():
  pass
  # os.system('cls' if os.name == 'nt' else 'clear')
  print("product popularity")

def leave_ebazaon():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Bye!")
  sys.exit()




def admin_menu():
  os.system('cls' if os.name == 'nt' else 'clear')

  print('Hello Admin, let me help you make products.')
  print('\n')
  print('Product name:')
  product_name = input('> ')

  print('Product price:')
  product_price = input('> ')

  with sqlite3.connect('bangazon.db') as conn:
    c = conn.cursor()

    c.execute("""
                insert into Product (ProductName, ProductPrice)
                values (?, ?)
              """,
                (product_name, product_price))
    conn.commit()



app_start()

