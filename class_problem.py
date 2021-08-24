class Item():

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def sell(self):
        print(f"{self.name} 아이템을 판매하였습니다")

    def shed(self):
        print(f"{self.name} 아이템을 버렸습니다")


class Shield(Item):

    def __init__(self, name, price, weight, wear_effect):
        super().__init__(name, price, weight)
        self.effect = wear_effect

    def wear(self):
        print("*** ---샤랄라--- ***")
        print("*** ------------- ***")
        print(f"{self.name} 아이템을 장착해서 {self.effect} 효과를 사용할 수 있습니다 ")
        print("*** ------------- ***")
        print("*** --- 샤랄라 --- ***") 

class Useable(Item):

    def __init__(self, name, price, weight, use_effect):
        super().__init__(name, price, weight)
        self.effect = use_effect

    def use(self):
        print("*** ---샤랄라--- ***")
        print("*** ------------- ***")
        print(f"{self.effect} 효과를 사용해서 {self.name}를 소모했습니다. ")
        print("*** ------------- ***")
        print("*** --- 샤랄라 --- ***") 

legendary_item = Item("majic_ring", 10000, 50)
legendary_item.shed()

general_item = Useable("약초", 50, 3, "5를 치유")
general_item.use()

