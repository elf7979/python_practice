version = 2.3

def printAuthor():
    print("저자의 이름은 하하하")

class Pay():

    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time

    def get_pay_info(self):
        print(f"{self.id} and {self.price} and {self.time}")
