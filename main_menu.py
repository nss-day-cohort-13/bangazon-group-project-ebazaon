import os
import sys
from user import *
from pay_opt import *
from order import *
from line_item import *

def start_menu():

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
      print("please pick one of the above options!")
      return(True)
  except ValueError:
      print("input the number next to your chosen option")
      return(True)


def create_customer_menu():

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

  # will call function for instantiating new user, to be added later

def choose_customer_menu():
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

start_menu()
