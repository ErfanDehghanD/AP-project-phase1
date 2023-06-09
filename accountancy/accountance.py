import os


class Accountancy:

    # this function appends every order to accountancy_output csv file
    def make_file(self, product_count, order_number, product_price, delivery_price):
        output = open('accountancy_output.csv', 'a')
        result = f'{product_count}, {str(order_number)}, {float(product_price) * int(product_count)}, {delivery_price},' \
                 f' {0.09 * float(product_price) * int(product_count)}'
        output.write(result)
        output.write("\n")
        output.close()

    # this function shows the accountancy_output csv file by CMD
    def show_file(self):
        os.system("start accountancy_output.csv")
        input("after closing the opened window, press enter to continue process...")
