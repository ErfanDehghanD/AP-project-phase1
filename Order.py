##########################################################
# import libraries
from random import randint
import os


class Order:

    def __init__(self):
        self.orderNumber = 0
        self.cardNumber = '0'
        self.address = 'address'
        self.phone_number = 'phone number'
        self.first_name = 'first name'
        self.last_name = 'last name'
        self.delivery_time = '0'


    def get_order(self):
        order_list = []
        entrance = input('do you want to make an order? ')
        order = eval(input('enter your product order like [product_name, product_number]'))
        resume = input()
        pass

    # this function makes order number with n digits
    def order_number(self):
        n = 11
        random_order_number = randint(10**(n-1), 10**n)
        self.orderNumber = random_order_number
        return random_order_number

    # this function checks card number validation by number of digits and input type
    def payment_validation(self, card_number):
        self.cardNumber = card_number
        if len(self.cardNumber) == 16 and type(eval(self.cardNumber)) == int:
            return True
        else:
            return False

    # this function makes a text expression for user to show the payment status
    def payment_validation_text(self):
        if self.payment_validation(self.cardNumber):
            return 'successful payment'
        else:
            return 'unsuccessful payment'

    # this function gets information needed for payment process
    def payment_information_set(self, address, phone_number, first_name, last_name, delivery_time):
        self.address = address
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.delivery_time = delivery_time

    # this function makes a file included (card_number, payment_validation_text(), first_name, last_name)
    def payment_output(self):
        output = open('payment_output.txt', 'x')
        result = f'{self.cardNumber}, {self.payment_validation_text()}, {self.first_name}, {self.last_name}'
        output.write(result)
        output.close()
        os.system("start payment_output.txt")
        input("after closing the opened window, press enter to continue process...")
        os.system("del payment_output.txt")

    # this function makes a file included:
    # (product_name, product_count, product_price, orderNumber, address,
    # first_name, last_name, delivery_time, delivery_type)
    # if (payment_validation() == True)
    def make_factor_constants(self, delivery_time, delivery_type):
        output = open('factor_output.txt', 'w')
        result1 = f'{self.orderNumber}, {self.address}, {self.first_name}, {self.last_name}'
        result2 = f'{delivery_time}, {delivery_type}'
        separator = "\n_______________________________________________________________"
        result = result1 + "|" + result2 + separator
        output.write(result)
        output.close()

    def make_factor_variables(self, product_name, product_count, product_price):
        output = open('factor_output.txt', 'a')
        result = f'{product_name}, {product_count}, {product_price}'
        output.write(result)
        output.close()

    def show_factor_output(self):
        os.system("start factor_output.txt")
        input("after closing the opened window, press enter to continue process...")
        os.system("del payment_output.txt")
