class Robot():
    def __init__(self, name, build_year):
        self.maker = "UofM"
        self.iswalking = True
        self.name = name
        self.build_year = build_year

hubo1 = Robot('mingming', 2020)
print(hubo1.maker, hubo1.iswalking, hubo1.name, hubo1.build_year)

hubo2 = Robot('sujin', 1983)
print(hubo2.maker, hubo2.iswalking, hubo2.name, hubo2.build_year)


