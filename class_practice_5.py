class Robot:
    population = 0
    maker = 'UofM'

    def __init__(self, name, build_year):
        self.iswalking = True
        self.name = name
        self.build_year = build_year
        self.xpos = 0
        self.ypos = 0
        Robot.population += 1   #생성자가 실행할 때마다 1씩 증가함 그리고 population은 모두가 공유하는 변수이기 때문에 robot과 hubo의 population 값은 동일

hubo1 = Robot('mingming', 2020)
hubo2 = Robot('shane', 2016)
hubo3 = Robot('sol', 2018)

print(Robot.maker, Robot.population, hubo1.population)

Robot.maker = 'Postech'
print(hubo2.maker, hubo2.population)