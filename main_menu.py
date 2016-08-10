import os
import sys
from user import *
from pay_opt import *
from order import *
from line_item import *
from product import *
from serialization import *

all_users = {}
all_pay_opt = {}
all_products = {}
all_orders = {}
all_order_line_items = {}

menu_display = True
menu_error = False
menu_not_num = False
user_login = False
username = None

def app_start():

    # Verify is working
    global all_users
    all_users = deserialize_users() #this will contain the entire dict of all users

    global all_pay_opt
    all_pay_opt = deserialize_pay_opt() #this will contain the entire dict of all pay options

    global all_products
    all_products = deserialize_products() #this will contain the entire dict of all users

    global all_orders
    all_orders = deserialize_orders() #this will contain the entire dict of all users

    global all_order_line_items
    all_order_line_items = deserialize_order_line_items() #this will contain the entire dict of all users

    start_menu()


def start_menu():

    global menu_display
    while menu_display == True:
      os.system('cls' if os.name == 'nt' else 'clear')

      print("*********************************************************")
      print("**  Welcome to Ebazaon! Command Line Ordering System!  **")
      print("*********************************************************")

      global user_login
      if user_login == True:
        print("\n")
        global username
        print("Welcome {}!".format(username))
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
      global menu_error
      menu_error = True
      return("invalid selection")
  except ValueError:
      global menu_not_num
      menu_not_num = True
      return("invalid selection")


def create_customer_menu():

  # Need to write in exception handlers for invalid input
  global menu_display
  menu_display = False

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

  # Verify is working
  user = User(name, address, city, state, zipcode, phone)
  all_users[user.uid.__str__] = user #make this an add users function then serialize it
  serialize_users()

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
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Which customer will be active?")
  # need to write a for loop that will go over deserialized list of user names and assign numbers to them as returned from function in user.py
  user_choice = input("> ")
  # needs to call the function that pulls the rest of the customer information
  # needs to return user's name for menu display
  global username
  username = # function for returned username

def create_pay_opt_menu():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Enter payment type (e.g. AmEx, Visa, Checking)")
  pay_type = input("> ")

  print("Enter account number")
  account = input("> ")
  # needs to run function to have user payment information added to file that holds that information
  added_pay_opt_success(pay_type)

def added_pay_opt_success(pay_type):
  os.system('cls' if os.name == 'nt' else 'clear')

  print("We successfully added {} as payment method. Press enter to continue.".format(pay_type))
  print("\n")
  input("> ")
  global menu_display
  menu_display = True
  start_menu()

def add_product_menu():
  # os.system('cls' if os.name == 'nt' else 'clear')
  print("please enter as many products as you need!")
  # needs to loop over deserialized product list and end with "done" option.
  # needs to display product list as long as "done" has not been hit.
  # Once done has been hit, it needs to go back to the main menu

def complete_order_menu():
  # os.system('cls' if os.name == 'nt' else 'clear')
  print("completing order")

def see_popularity_menu():
  # os.system('cls' if os.name == 'nt' else 'clear')
  print("product popularity")

def leave_ebazaon():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Bye!")
  sys.exit()

app_start()

