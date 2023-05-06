from warehouse.warehouse import *
from logestic.logestic  import logestic
from accountancy.accountance import Accountancy
from order.Order import Order
#import pdb ; pdb.set_trace()

print("Welcome")

inswarehouse = warehouse()
inswarehouse.load_warehouse()
insaccountancy=Accountancy()
insaccountancy.init_file()

while True:
    print("How do you want to enter the shop?")
    print("1.as a customer 2.as a manager  Enter the number")
    a = int(input())
    if a == 1 :
        inswarehouse.show_warehouse_supply()
        
        first_name = input("enter your firstname please")
        last_name = input("your lastname please")
        phone_number = input("your phone number please")
        address = input("your address please")
        

        ins1 = Order()
        order_number = ins1.order_number()

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
        
        

        county = input("enter your county")
        city = input ("enter your city")
        postal_code = input("enter your postal code")
        ins2 = logestic(county, city, address, postal_code)

        ins2.init_counters()
        ins2.available_time()
        delivery_time = input("enter the time from options") 
        ins2.delivery_time(delivery_time)
        ins2.save_counters()

        delivery_type = ins2.county_check()

        ins1.payment_information_set(address, phone_number, first_name, last_name, delivery_time)
        card_number = input("enter your card number  :  ")
        ins1.payment_validation(card_number)
        ins1.payment_validation_text()
        ins1.payment_output()
        
        if ins1.payment_validation():
            ins1.show_factor_output()
            insaccountancy.make_file(product_count, order_number, product_price, delivery_price)
              

    elif a == 2 :
        try:
            from playsound import playsound
            playsound('audio.mp3')
        except Exception:
            pass
        
        
        print('heil hitler',end=' ')
        while True:
            print('what do you want to do with your shop ?')
            print('1. I want to look into my warehouse')
            print('2. I want to look into my accountancy')
            inswarehouse.load_warehouse() 
            choice_1_manager = input('enter your command (1 or 2) here : ')
            
            if choice_1_manager=='1':
                print('what do you want to do with ware house :')
                print('1. look at warehouse supplies')
                print('2. add new product to warehouse')
                print('3. update warehouse stock')
                choice_2_manager=input('enter your command (1 or 2 or 3) here :')
                
                if choice_2_manager=='1':
                    inswarehouse.show_warehouse_supply()
                elif choice_2_manager=='2':
                    num=input('how many new products you want to add : ')
                    for i in range(int(num)):
                        try:
                            product=input('please enter the name of new product : ')
                            price=str(float(input('please enter the price of new product : ')))
                            count=str(int(input(f'how many of {product} you have ? ')))
                            product_number=input('please give a specific id for product :')
                            inswarehouse.add_product(product_number,product,price,count)
                            print('----------------------------------------------------------')
                            inswarehouse.save_warehouse()
                        except Exception:
                            print('please enter attributes correctly')
                    
                elif choice_2_manager=='3':
                    print('how do you like to update your warehouse stock ?')
                    print('1.by consule')
                    print('2.by text file')
                    print('3.by csv file')
                    choice_3_manager=input('enter your command (1 or 2 or 3) here :')
                    if choice_3_manager == '1':
                        situation='yes'
                        while situation!='no':
                            product_number=input('please enter id of product you want to update : ')
                            new_count=input('how many of this product is in the warehouse : ')
                            inswarehouse.update_by_consule(product_number,new_count)
                            situation=input('do you want update another product (yes/no) : ').lower()
                            while situation not in 'yes no':
                                situation=input('please enter your command correctly (yes/no) : ').lower()
                            print('--------------------------------------------------------------')
                    
                    elif choice_3_manager=='2':
                        inswarehouse.update_manually_txt()

                    elif choice_3_manager=='3':
                        inswarehouse.update_manually_csv()
                    
                    inswarehouse.save_warehouse()                        
                    
                    
                    
            if choice_1_manager=='2':
                insaccountancy.show_file()
                
            
            #kaftar kakol be sar hay hay
            #in khabar az man bebar hay hay
            #bego be yaram ke dosesh daram 
            #be bargarde cheshberasham man khaterkhasham
            
