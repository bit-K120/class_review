class Customer:
    def __init__(self,first_name,family_name, age): #オブジェクトの起動
        self.first_name = first_name
        self.family_name = family_name
        self.age = age 

    def full_name(self): #名前と名字をあわせる関数
        full_name = f"{self.first_name} {self.family_name}"
        return full_name

    def entry_fee(self):
        if self.age < 20:
            entry_fee = 1000
        elif 19 < self.age < 65:
            entry_fee = 1500
        elif 64 < self.age:
            entry_fee = 1200
        elif self.age <= 3:
            entry_fee = 0
        elif 75 <= self.age:
            return 500
        return entry_fee
    
    def info(self):
        info = self.full_name(),self.age,self.entry_fee()
        return info

    def info_csv(self):
        info_result = self.info()
        info_csv = f'"{info_result[0]},{info_result[1]},{info_result[2]}"'
        return info_csv
    
    def tab_split(self):
        data_to_split = self.info()
        tab_split = f"{data_to_split[0]}\t{data_to_split[1]}\t{data_to_split[2]}"
        return tab_split
    
    def pipe_split(self):        
        data_to_split = self.info()
        pipe_split = f"{data_to_split[0]}{'|'}{data_to_split[1]}{'|'}{data_to_split[2]}"
        return pipe_split

       
    

ken = Customer(first_name="Ken",family_name="Tanaka", age = 15)
print(ken.full_name())
print(ken.age)
print(ken.entry_fee())
print(ken.info_csv())
tom = Customer(first_name="Tom", family_name="Ford", age = 57)
print(tom.full_name())
print(tom.age)
print(tom.entry_fee())
print(tom.info_csv())
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age= 73)
print(ieyasu.age)
print(ieyasu.entry_fee())
print(ieyasu.info_csv())

shohei = Customer(first_name = "Shohei", family_name = "Ohtani", age = 3 )
print(shohei.entry_fee())

buffet = Customer(first_name= "Warren", family_name= "Buffet", age = 75)
print(buffet.entry_fee())

ken = Customer(first_name="Ken",family_name="Tanaka", age = 15)
tom = Customer(first_name="Tom", family_name="Ford", age = 57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age= 73)
print(ken.tab_split())
print(tom.tab_split())
print(ieyasu.tab_split())

ken = Customer(first_name="Ken",family_name="Tanaka", age = 15)
tom = Customer(first_name="Tom", family_name="Ford", age = 57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age= 73)
print(ken.pipe_split())
print(tom.pipe_split())
print(ieyasu.pipe_split())


