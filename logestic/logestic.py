import os
# determining cities of the counties
# 1=> tehran = 1   (tehran county just have a city)
# 2=> esphahan = 1 / ghahjavarestan = 2
# 3=> tabriz = 1 / sardorud = 2

class logestic:
    def __init__(self, county, city, address, postal_code):
        self.county = county
        self.city = city
        self.address = address
        self.postal_code = postal_code

        self.ncounter = 0
        self.ecounter = 0

    def county_check(self):
        if self.county == 1 :
            return "courier"
        else :
            return "post"
       
    def save_counters(self):
        output = open('logestic\counters.txt', 'w')
        result = f'[{self.ncounter}, {self.ecounter}]'
        output.write(result)
        output.close()

    def init_counters(self):
        file = open("logestic\counters.txt", 'r')
        if os.path.isfile("logestic\counter.txt"):
            self.ncounter = file [0]
            self.ecounter = file [1]
        else:
            pass
    def delivery_price(self):
        if self.county == 1:
            return 5
        elif self.county == 2 and self.city == 1:
            return 10
        elif self.county == 2 and self.city == 2:
            return 11
        elif self.county == 3 and self.city == 1:
            return 15
        elif self.county == 3 and self.city == 2:
            return 17
    
    # morining, noon and evening
    def available_time(self):
        if self.ncounter <= 3 and self.ecounter <= 3:
            print("when do you want your order to be delivered ?  1.morning  2.noon 3.evening   :    ")

        elif self.ecounter <= 3 and self.ncounter > 3:
            print("when do you want your order to be delivered ?  1.morning  3.evening   :    ")

        elif self.ncounter <= 3 and self.ecounter > 3:
            print("when do you want your order to be delivered ?  1.morning  2.noon   :    ")

        elif self.ncounter > 3 and self.ecounter > 3 :
            print("when do you want your order to be delivered ?  1.morning      :      ")

    def delivery_time(self, delivery_time):
        if delivery_time == "noon" :
            self.ncounter += 1
            print("It will be delivered at noon")

        elif delivery_time == "evening":
            self.ecounter += 1
            print("It will be delivered in the evening")

        else :
            print("It will be delivered in the morning")
        

    


