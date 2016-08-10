import os
import sys
from user import *
from pay_opt import *
from orders import *
from line_item import *
from products import *
import serialization

all_users = {}
all_pay_opt = {}
all_products = {}
all_orders = {}
all_order_line_items = {}
main_menu_display = True
main_menu_error = False
main_menu_not_num = False

def app_start():

    global all_users
    all_users = serialization.deserialize_users() #this will contain the entire dict of all users

    global all_pay_opt
    all_pay_opt = serialization.deserialize_pay_opt() #this will contain the entire dict of all pay options

    global all_products
    all_products = serialization.deserialize_products() #this will contain the entire dict of all users

    global all_orders
    all_orders = serialization.deserialize_orders() #this will contain the entire dict of all users

    global all_order_line_items
    all_order_line_items = serialization.deserialize_order_line_items() #this will contain the entire dict of all users


def start_menu():

    global main_menu_display
    while main_menu_display == True:
      os.system('cls' if os.name == 'nt' else 'clear')

      print("*********************************************************")
      print("**  Welcome to Ebazaon! Command Line Ordering System!  **")
      print("*********************************************************")
      print("1. Create a customer account")
      print("2. Choose active customer")
      print("3. Create a payment option")
      print("4. Add product to shopping cart")
      print("5. Complete an order")
      print("6. See product popularity")
      print("7. Leave Ebazaon!")
      print("\n")

      global main_menu_error
      if main_menu_error == True:
        main_menu_error = False
        print("Please choose a number within option range")

      global main_menu_not_num
      if main_menu_not_num == True:
        main_menu_not_num = False
        print("Please choose a number to indicate your selection")

      menu_selection = input("> ")
      route_user_selection(menu_selection)


def route_user_selection(selection):

  try:
    if int(selection) == 1:
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
      global main_menu_error
      main_menu_error = True
      return("invalid selection")
  except ValueError:
      global main_menu_not_num
      main_menu_not_num = True
      return("invalid selection")


def create_customer_menu():

  global main_menu_display
  global all_users
  main_menu_display = False

  os.system('cls' if os.name == 'nt' else 'clear')

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

  print("Enter phone number")
  phone = input("> ")

  user = User(name, address, city, state, zipcode, phone)
  all_users[user.uuid.__str__()] = user #make this an add users function then serialize it
  print(all_users)
  serialization.serialize_users(all_users)
  # will call function for instantiating new user, to be added later
  cust_create_success(name)

def cust_create_success(name):

  os.system('cls' if os.name == 'nt' else 'clear')

  print("We successfully added {} as a user.\n Press enter to continue.".format(name))
  print("\n")
  input("> ")
  global main_menu_display
  main_menu_display = True
  start_menu()


def choose_customer_menu():
  global all_users
  for key, value in all_users.items():
    print(value.name)
  input('') # this is just to stop it from running the app_start() again
  print("choosing user")

def create_pay_opt_menu():
  print("creating payment")

def add_product_menu():
  print("adding products")

def complete_order_menu():
  print("completing order")

def see_popularity_menu():
  print("product popularity")

def leave_ebazaon():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Bye!")
  sys.exit()

app_start()
start_menu()
