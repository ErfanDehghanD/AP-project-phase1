# hello logestics
print(" hello logestics ")
print(" It's a nice day don't you agree ")
print(" whuaaaa ")

# determining cities of the counties
# 1=> tehran = 1   (tehran county just have a city)
# 2=> esphahan = 1 / ghahjavarestan = 2
# 3=> tabriz = 1 / sardorud = 2

# where these datas come from ??????????????????????????
class Logestics:
    def __init__(self, county, city, address, postal_code):
        self.county = county
        self.city = city
        self.address = address
        self.postal_code = postal_code

        self.ncounter = 0
        self.ecounter = 0

    def county_check(self):
        if self.county == 1 :
            print("It will be delivered by courier")
        else :
            print("It will be posted")
        
    # morining, noon and evening
    # what about the day ?????????????????
    # which one is in priority to check if its full ... ??????????????????????
    def delivery_time(self):
        if self.ncounter <= 3 :
            self.ncounter += 1
            print("It will be delivered at? noon")

        elif self.ecounter <= 3:
            self.ecounter += 1
            print("It will be delivered in the evening")

        else :
            print("It will be delivered in? morning")
        

    


