# class Robot:
#     pass

# robot1 = Robot()
# robot1.name = 'Hubo 2'
# robot1.weight = '45 kg'

# robot2 = Robot()
# robot2.name = 'Hubo 2 Plus'
# robot2.build_year = '2011'

# print(robot1.name, '-', robot1.weight)
# print(robot2.name, '-', robot2.build_year)

class Robot:

    def __init__(self):
        self.name = 'mingmingbot'
        self.weight = '2.2kg'

hubo1 = Robot()
hubo2 = Robot()

print(hubo1.name, hubo1.weight)
print(hubo2.name, hubo2.weight)

print()

hubo1.name = "sujinbot"
hubo2.weight = '23kg'

print(hubo1.name, '-', hubo1.weight)
print(hubo2.name, '-', hubo2.weight)
