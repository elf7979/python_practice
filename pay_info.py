import pay_module
from pay_module import Pay

print(pay_module.version)
pay_module.printAuthor()

pay_info = pay_module.Pay('ming', 1000000, "2021-08-25")
pay_info.get_pay_info()

if __name__ == "__main__":
    print("pay module 실행")


print(__name__)
print(pay_module.__name__)