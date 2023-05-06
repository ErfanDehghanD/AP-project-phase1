from warehouse.warehouse import *
from logestic.logestic  import logestic
from accountancy.accountance import Accountancy
from order.Order import Order


print("Welcome")

inswarehouse = warehouse()

while True:
    print("How do you want to enter the shop?")
    print("1.as a customer 2.as a manager  Enter the number")
    a = input()
    if a == 1 :
        inswarehouse.show_warehouse_supply()
        
        first_name = input("enter your firstname please")
        last_name = input("your lastname please")
        phone_number = input("your phone number please")
        address = input("your address please")

        ins1 = Order()
        ins2 = logestic()
        order_number = ins1.order_number()

        ins2.available_time()
        delivery_time = input("enter the time from options") #how to save ncounter to check ?? 
        ins2.delivery_time(delivery_time)
        delivery_type = ins2.county_check()  # input of address ???


        ins1.make_factor_constants(delivery_time, delivery_type)
        while True:
            product_name = input("Enter product ID you want to order    :    ")
            product_count = input("How many of this product do you want to order?    :    ")
            inswarehouse.update_order(product_name, product_count)
            check_continue = input("do you want to add new products to your order?  yes /  no   :")
            product_price = inswarehouse.get_price()  # ...
            ins1.make_factor_variables(product_name , product_count, product_price)

            if check_continue == "no":
                break
        
        ins1.payment_information_set(address, phone_number, first_name, last_name, delivery_time)
        card_number = input("enter your card number  :  ")
        ins1.payment_validation(card_number)
        ins1.payment_validation_text()
        ins1.payment_output()
        
        if ins1.payment_validation():
            ins1.show_factor_output()
            
              

    elif a == 2 :
        print("What do you want to do?  1.inventory 2.accounting")
        b = input()
        if b == 1:
            print("Which part of warehousing are you interested in? ")
            print("1.show warehouse inventory")
            print("2.updating inventory")
            print("3.adding new products")
            c = input ()
            #      ....      ?


        elif b == 2:
            print("       connecting to accounting      ???")
        

