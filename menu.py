import os
import sys
import pickle
import uuid
from pay_opt import *
from user import *
from serialization import *

class Menu():

  # main_menu_display = True
  # main_menu_error = False
  # main_menu_not_num = False

  def start_menu(self):


    # while self.main_menu_display == True:
      # os.system('cls' if os.name == 'nt' else 'clear')

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

      # if self.main_menu_error == True:
      #   self.main_menu_error = False
      #   print("Please choose a number within option range")

      # if self.main_menu_not_num == True:
      #   self.main_menu_not_num = False
      #   print("Please choose a number to indicate your selection")




    menu_selection = input("> ")
    self.route_user_selection(menu_selection)


  def route_user_selection(self, selection):

    # try:
      if int(selection) == 1:
        self.create_customer_menu()
      elif int(selection) == 2:
        self.choose_customer_menu()
      elif int(selection) == 3:
        self.create_pay_opt_menu()
      elif int(selection) == 4:
        self.add_product_menu()
      elif int(selection) == 5:
        self.complete_order_menu()
      elif int(selection) == 6:
        self.see_popularity_menu()
      elif int(selection) == 7:
        self.leave_ebazaon()
    #     self.main_menu_error = True
    #     return("invalid selection")
    # except ValueError:
    #     self.main_menu_not_num = True
    #     return("invalid selection")


  def create_customer_menu(self): #create customer

    # self.main_menu_display = False
    # os.system('cls' if os.name == 'nt' else 'clear')

    deserializeUser(self)
    uid = str(uuid.uuid4())
    self.userDict[uid] = dict()

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
    user.__dict__
    self.userDict[uid] = user

    serializeUser(self)

    print(self.userDict)


  # def cust_create_success(name):

  # os.system('cls' if os.name == 'nt' else 'clear')

  # print("We successfully added {} as a user.\n Press enter to continue.".format(name))
  # print("\n")
  # input("> ")
  # global main_menu_display
  # main_menu_display = True
  # start_menu()


  def choose_customer_menu(self): #choose a customer
      deserializeUser(self)
      print("Select a customer account.")
      self.showUserName()
      userSelect = input(">")
      userID = self.showUserID(userSelect)
      print(userID)


  def showUserName(self): # prints list of Customer/Users names
                          #currently only being used within choose_customer funciton
    u = self.userDict
    for k,v in u.items():
      print(v['name'])

  def showUserID(self, inp): # once a Customer/User is selected return the corresponding userID
                            #currently only being used within choose_customer funciton
    u = self.userDict
    for k,v in u.items():
      if inp == v['name']:
        return k


  def create_pay_opt_menu(self): #create payment option
                                # ***** still needs customer id passed in as attribute *****

    deserializePayment(self)
    uid = str(uuid.uuid4())
    self.paymentDict[uid] = dict()

    print("Select a payment option")
    print("Visa")
    payment_name = input("> ")


    print("Enter account number.")
    account = input("> ")


    payment = Pay_Option(payment_name, account) #***** <-- (cust_uid) as 3rd argument *****

    self.paymentDict[uid] = payment.__dict__

    serializePayment(self)

    print(self.paymentDict)






  # def add_product_menu(): ***** product menu will need to be created so user cannot create own products *****


  #   deserializeProduct(self)
  #   uid = str(uuid.uuid4())
  #   self.productDict[uid] = dict()

  #   print("Choose your products")
  #   product_name = input("> ")


  #   print("Enter account number.")
  #   account = input("> ")

  #   product = Product(product_name, product_price)

  #   self.productDict[uid] = product.__dict__

  #   serializeproduct(self)

  #   print(self.productDict)






  # def complete_order_menu(self): ***** need to pass in userID and payID as attributes and run a choose_payment function within *****

  #   deserializeOrder(self)
  #   uid = str(uuid.uuid4())
  #   self.orderDict[uid] = dict()

  #   print("Your order total is X. Ready to purchase?")
  #   print ("Y/N")

  #   if user enters Y

      # run choose_payment_option()

  #   order = Order(cust_uid, pay_opt_uid, paid)

  #   self.orderDict[uid] = order.__dict__

  #   serializeorder(self)

  #   print(self.orderDict)






  # def see_popularity_menu(self):

#     Product           Orders     Customers  Revenue
# *******************************************************
# AA Batteries      100         20        $990.90
# Diapers           50          10        $640.95
# Case of Cracki... 40          30        $270.96
# *******************************************************
# Totals:           190         60        $1,902.81

# -> Press any key to return to main menu






  # def create_line_items(self):  ***** need to pass in productID and orderID as attributes ******

  #   deserializeLineItems(self)
  #   uid = str(uuid.uuid4())
  #   self.lineItemsDict[uid] = dict()

  #   lineItems = LineItems(productID, orderID)

  #   self.lineItemsDict[uid] = lineItems.__dict__

  #   serializeLineItems(self)

  #   print(self.lineItemsDict)






# def leave_ebazaon():
#   os.system('cls' if os.name == 'nt' else 'clear')
#   print("Bye!")
#   sys.exit()

# app_start()
# start_menu()



if __name__ == '__main__':
  menu = Menu()
  menu.start_menu()

