##########################################################
# import libraries
from random import randint


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
    def payment_validation(self):
        card_number = input('input your card number for successful payment... ')
        self.cardNumber = card_number
        if len(self.cardNumber) == 16 and type(eval(self.cardNumber)) == int:
            return True
        else:
            return False

    # this function makes a text expression for user to show the payment status
    def payment_validation_text(self):
        if self.payment_validation():
            return 'successful payment'
        else:
            return 'unsuccessful payment'

    # this function gets information needed for payment process
    def payment_information(self):
        self.address = input('input your address as necessary information... ')
        self.phone_number = input('input your phone number as necessary information... ')
        self.first_name = input('input your first name as necessary information... ')
        self.last_name = input('input your last name as necessary information... ')
        self.delivery_time = input('input your proper delivery time as necessary information... ')
        return self.address, self.phone_number, self.first_name, self.last_name, self.delivery_time

    # this function makes a file included (card_number, payment_validation(), first_name, last_name)
    def payment_output(self):
        output = open('C:\Users\1\Desktop\Sharif\4\برنامه‌نویسی پیشرفته\Project1\payment_output', 'x')
        result = f'{self.cardNumber}, {self.payment_validation_text()}, {self.first_name}, {self.last_name}'
        output.write(result)

    # this function makes a file included:
    # (product_name, product_price, order_number(), address, first_name, last_name, delivery_time, delivery_type)
    # if (payment_validation() == True)
    def factor_output(self):
        if self.payment_validation() == True:
            # add product_name, product_price at begin (from somewhere)
            # add delivery_type at the end (from logistic class)
            return self.order_number(), self.address, self.first_name, self.last_name, self.delivery_time
        else:
            pass

