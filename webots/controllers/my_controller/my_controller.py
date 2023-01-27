"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor

#Needed informations : 

# https://cyberbotics.com/doc/guide/tutorial-4-more-about-controllers?tab-language=python -> Lesson
# https://cyberbotics.com/doc/guide/khepera3 -> Robot parameters 

from controller import *
from math import * 
import time

class FugitiveRobot(Robot):
    def __init__(self):
         super().__init__()
         self.__motors = FugitiveRobotMotors()
         self.__distances = FugitiveRobotSensors()
         self.__gps = FugitiveRobotGPS()
         
    def run(self, backward=False, forward=False, left=False, right=False):
        if (forward == True) : 
            self.__motors.go_front()
        if(backward == True) : 
            self.__motors.go_back()
        if(left == True) : 
            self.__motors.go_left()
        if(right == True) : 
            self.__motors.go_right()

    def distance_detection(self):
        return self.__distances.getDistanceValue()

    def coordinates(self, timestep):
        self.__gps.enable(timestep)
        return self.__gps.getCoordinates()

    def move(self):

        distance = self.distance_detection()
        print(distance)
        
        if (distance > 100):
            #self.run(backward=True, left=True)
            print("Recule, bip, bip")
        else:
            self.run(forward=True)

    def checkArenaCoordinates(self):

        border = { 
            "left":-3.5,
            "right":3.5,
            "front":3.5,
            "back":-3.5
        }

        mapLimit = 0.2

        coordinates = self.coordinates(timestep) 

        distances = []

        for key, value in border.items():
            distances.append(abs(coordinates[0]-border[key]))
            distances.append(abs(coordinates[1]-border[key]))
        distances = min(distances)

        if(distances < mapLimit): 
            print("Arrêt nécessaire")
        print(distances)   

class FugitiveRobotMotor(Motor): 

    def __init__(self, name=None):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)

class FugitiveRobotMotors():
    def __init__(self):
        self.__left_wheel_motor = FugitiveRobotMotor('left wheel motor')
        self.__right_wheel_motor = FugitiveRobotMotor('right wheel motor')

    def go_front(self):
        self.__left_wheel_motor.setVelocity(5)
        self.__right_wheel_motor.setVelocity(5)

    def go_back(self):
        self.__left_wheel_motor.setVelocity(-5)
        self.__right_wheel_motor.setVelocity(-5)

    def go_left(self):
        self.__left_wheel_motor.setVelocity(-5)
        self.__right_wheel_motor.setVelocity(5)

    def go_right(self):
        self.__left_wheel_motor.setVelocity(5)
        self.__right_wheel_motor.setVelocity(5)
    
class FugitiveRobotSensors():
    def __init__(self):

        self.__ds = []
        for i in range(11):
            self.__ds.append(DistanceSensor(f'ds{i}')) 

        self.__us = []
        for j in range(5):
            self.__us.append(DistanceSensor(f'us{j}'))
    
    def enable(self,timestep:int) -> None :

        for i in range(len(self.__ds)):
            self.__ds[i].enable(timestep)

        for j in range(len(self.__us)):
            self.__us[j].enable(timestep)

    def getDistanceValue(self):

        for i in range(11):
            for j in range(5):
                #return self.__ds[i].getValue(),self.__us[j].getValue()]
                #return self.__ds[5].getValue()
                return self.__ds[i].getValue()
        #return self.__ds[0].getValue()

class FugitiveRobotGPS():
    # def getCoordinates(self):
    #     return self.__gps.getValues()

    def __init__(self):
        self.__gps = GPS('gps')
    
    def enable(self,timestep:int) -> None :
        self.__gps.enable(timestep)

    def getCoordinates(self):
        return self.__gps.value[0], self.__gps.value[1]

robot = FugitiveRobot()
timestep = int(robot.getBasicTimeStep())

i = 0

while robot.step(timestep) != -1:
    pass
    # Read the sensors:
    # Enter here functions to read sensor data, like:

    #val = robot.distance_detection() 
    # if(not i%10):
        #     print(val)
        # i = i+1

    #val = robot.coordinates(timestep)

    robot.move()

    # robot.run(forward=True)
    # robot.checkArenaCoordinates()

    #robot.run()

