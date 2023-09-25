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
        return entry_fee
    
    def info(self):
        info = self.full_name(),self.age,self.entry_fee()
        return info

    def info_csv(self):
        info_result = self.info()
        info_csv = f'"{info_result[0]},{info_result[1]},{info_result[2]}"'
        return info_csv

ken = Customer(first_name="Ken",family_name="Tanaka", age = 15)
print(ken.full_name())
print(ken.age)
print(ken.entry_fee())
print(ken.info())
