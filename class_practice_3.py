class Robot():
    def __init__(self, name, build_year):
        self.maker = 'UofM'
        self.iswalking = True
        self.name = name
        self.build_year = build_year
        self.xpos = 0
        self.ypos = 0

    def move(self):
        if self.iswalking:
            self.xpos += 1
            self.ypos += 1

    def curPosition(self):
        print('current location: ({}, {})'.format(self.xpos, self.ypos))

hubo = Robot('shane', 2016)
hubo.move()
hubo.move()
hubo.move()
hubo.curPosition()