# section_117.py

class Robot():

    def speak(self):
        print("Robot speaks")

    def move(self):
        print("Robot moves")

    def charge(self):
        print("Robot charges")

class CleanRobot(Robot):
    def broom(self):
        print("Robot cleans dust")

robot = Robot()
robot.move()

clean = CleanRobot()
clean.broom()
clean.move()