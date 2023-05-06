import os

def split_by_comma(string):
    return string.split(",")

def find_index_count(L:list,x):
    for i in range(len(L)):
        if L[i][0]==x:
            return i
    
def new_csv(L:list):
    columns=""
    for i in L:
        columns=columns+f'{i},'
    os.system(f'echo {columns}>temporary_csv.csv')
    os.system('start temporary_csv.csv')
    
def new_txt():
    os.system('echo please enter your entery like this : (product number,count):(5,14)(11,2)>temporary_text.txt')
    with open('temporary_text.txt','a') as txt:
        txt.write('\n(product number,count):')
        
    os.system('start temporary_text.txt')
    
def csv_to_dataframe(address):
    with open(address,'r') as csv:
        dataframe=csv.read().split('\n')
        dataframe.remove("")
        dataframe=list(map(split_by_comma,dataframe))
        return dataframe

def text_to_dataframe(address):
        with open(address,'r') as txt:
            tuple_line=txt.read().split('\n')[2]
        
        dataframe=[]
        string_tuple=''
        status=0
        for i in tuple_line:
            if i==')':
                status=0
                string_tuple=string_tuple+'")'
                dataframe.append(list(eval(string_tuple)))
                string_tuple=''
            if i==',':
                string_tuple=string_tuple+'"'        
            if status:
                string_tuple=string_tuple+i            
            if i=='(':
                status=1
                string_tuple=string_tuple+'("'
            if i==',':
                string_tuple=string_tuple+'"'
        
        return dataframe

def column_maker(L):
    len_0 = len((L[0])[0])
    len_1 = len((L[0])[1])
    len_2 = len((L[0])[2])
    len_3 = len((L[0])[3])
    lens = [len_0, len_1, len_2, len_3]
        
    for i in L:
        result = ""
        for j in i:
            if i.index(j) == 0:
                space_num = lens[0] - len(j)
            elif i.index(j) == 1:
                space_num = lens[1] - len(j)
            elif i.index(j) == 2:
                space_num = lens[2] - len(j)
            elif i.index(j) == 3:
                space_num = lens[3] - len(j)
            result += j
            result += (space_num+10) * " "
        print(result)       
        


class warehouse:
    def __init__(self):
        self.warehouse=csv_to_dataframe('warehouse.csv')
        
    def add_product(self,product_number,product,price,count):
        self.warehouse.append([product_number,product,price,count])
        
    def update_order(self,product_number,count):
        I=find_index_count(self.warehouse, product_number)
        if int(self.warehouse[I][3])-int(count)>0:
            self.warehouse[I][3]=str(int(self.warehouse[I][3])-int(count))
        else:
            print('there is not enough products in this warehouse')
    
    def update_by_consule(self,product_number,new_count):
        try :
            i=find_index_count(self.warehouse, product_number)
            self.warehouse[i][3]=new_count
        except TypeError:
            print(f'entered product number {product_number} is incorrect')
    
    def update_manually_csv(self):
        new_csv(['product number','count'])
        input('edit and save opened window than close it and press enter to continue ...')
        df=csv_to_dataframe('temporary_csv.csv')
        try:
            for i in df :
                index=find_index_count(self.warehouse,i[0])
                self.warehouse[index][3]=i[1]
            self.show_warehouse_supply()   
        except TypeError:
            print(f'entered product number {i[0]} is incorrect')
        os.system('del temporary_csv.csv')
        
    def update_manually_txt(self):
        new_txt()
        input('edit and save opened window than close it and press enter to continue ...')
        df=text_to_dataframe('temporary_text.txt')
        try:
            for i in df :
                index=find_index_count(self.warehouse,i[0])
                self.warehouse[index][3]=i[1]
            self.show_warehouse_supply()     
        except TypeError:
            print(f'entered product number {i[0]} is incorrect')
        os.system('del temporary_text.txt')
    
    def show_warehouse_supply(self):
        column_maker(self.warehouse)    
    
    def save_warehouse(self):
        with open('warehouse.csv','w') as csv:
            csv.write('')
        with open('warehouse.csv','a') as csv:
            for i in self.warehouse:
                for j in i:
                    csv.write(f'{j},')
                csv.write('\n')
        print('warehose successfully saved')

x=warehouse()
x.show_warehouse_supply()
x.update_by_consule('6','8')
x.show_warehouse_supply()
x.save_warehouse()
x.update_manually_csv()
