class Human:
    """人間を表すクラス"""
    species = "ホモサピエンス"

    def __init__(self,name,height,weight,age):#インスタンス
        self.name = name
        self.height = height
        self.weight = weight
        self._height_meter = self._calc_meter()
        self._age = 0

    def talk(self):
        print(f"こんにちは{self.name}です。")

    def walk(self):
        print(f"{self.name}は歩きます。")

    def _calc_meter(self):
        return self.height /100
    
    @property
    def bmi(self):
        return self.weight / self._height_meter **2

    @property
    def age(self,age):
        return self._age

    @age.setter
    def age(self,value):
        try:
            value= int(value)
        except ValueError:
            raise ValueError("ageは整数で指定してください。")
        if value < 0:
            raise ValueError("ageは整数で指定してください。")
        self._age = value

class Customer(Human):
    """顧客を表すクラス"""
    def __init__(self,name,height,weight,age,customer_number):
        super().__init__(name,height,weight,age)
        self.customer_number = customer_number

ikuma = Customer("ikuma",170,60,20,1)
print(ikuma.name,ikuma.height,ikuma.weight)
ikuma.walk
print(ikuma._height_meter)
print(ikuma.species)
print(ikuma.customer_number)

print()

sato = Human("sato",160,50,42)
print(sato.name,sato.height,sato.weight)
sato.walk
print(sato.bmi)

