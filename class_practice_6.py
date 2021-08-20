class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.__build_year = build_year  #네임 맹글링 이름 바꾸기 기법
        self.xpos = 0
        self.ypos = 0

    def getYear(self):
        return self.__build_year

hubo = Robot('mingming', 2020)

hubo.name = 'Albert'

print(hubo.name)
print(hubo.getYear(), hubo.name)

print()
print(dir(hubo))