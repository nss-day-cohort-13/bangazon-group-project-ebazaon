import os
import sys
from user import *
from pay_opt import *
from order import *
from line_item import *

def start_menu():

  while True:
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
    print("7. Leave Bangazon!")

    menu_selection = input("> ")
    route_user_selection(menu_selection)

def route_user_selection(selection):
  try:
    if int(selection) == 1:
      print("creating account")
      return(False)
    elif int(selection) == 2:
      print("choosing user")
      return(False)
    elif int(selection) == 3:
      print("creating payment")
      return(False)
    elif int(selection) == 4:
      print("adding products")
      return(False)
    elif int(selection) == 5:
      print("completing order")
      return(False)
    elif int(selection) == 6:
      print("product popularity")
      return(False)
    elif int(selection) == 7:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Bye!")
      sys.exit()
    else:
      print("please pick one of the above options!")
      return(True)
  except ValueError:
      print("input the number next to your chosen option")
      return(True)


def create_customer_menu():

  print("Enter customer name")
  input("> ")

  print("Enter street address")
  input("> ")

  print("Enter city")
  input("> ")

  print("Enter state")
  input("> ")

  print("Enter postal code")
  input("> ")

  print("Enter phone number")
  input("> ")

def choose_customer_menu():
  pass

def create_pay_opt_menu():
  pass

def add_product_menu():
  pass

def complete_order_menu():
  pass

def see_popularity_menu():
  pass

def leave_ebazaon():
  pass

start_menu()
