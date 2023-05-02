import os


class Accountancy:

    def init_file(self):
        output = open('accountancy_output.csv', 'x')
        result = "product count, order id, total price, delivery price, tax"
        output.write(result)
        output.close()

    def make_file(self, product_count, order_number, product_price, delivery_price):
        output = open('accountancy_output.csv', 'a')
        result = f'{product_count}, {order_number}, {float(product_price) * int(product_count)}, {delivery_price},' \
                 f' {0.09 * float(product_price) * int(product_count)}'
        output.write(result)
        output.close()

    def show_file(self):
        os.system("start accountancy_output.csv")
        input("after closing the opened window, press enter to continue process...")
