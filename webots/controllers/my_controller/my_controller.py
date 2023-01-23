"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor

#Needed informations : 

# https://cyberbotics.com/doc/guide/tutorial-4-more-about-controllers?tab-language=python -> Lesson
# https://cyberbotics.com/doc/guide/khepera3 -> Robot parameters 

from controller import *

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
        self.__ds0_sensor = DistanceSensor('ds0')
        self.__ds1_sensor = DistanceSensor('ds1')
        self.__ds10_sensor = DistanceSensor('ds10')
        self.__ds2_sensor = DistanceSensor('ds2')
        self.__ds3_sensor = DistanceSensor('ds3')
        self.__ds4_sensor = DistanceSensor('ds4')
        self.__ds5_sensor = DistanceSensor('ds5')
        self.__ds6_sensor = DistanceSensor('ds6')
        self.__ds7_sensor = DistanceSensor('ds7')
        self.__ds8_sensor = DistanceSensor('ds8')
        self.__ds9_sensor = DistanceSensor('ds9')
        self.__us0_sensor = DistanceSensor('us0')
        self.__us1_sensor = DistanceSensor('us1')
        self.__us2_sensor = DistanceSensor('us2')
        self.__us3_sensor = DistanceSensor('us3')
        self.__us4_sensor = DistanceSensor('us4')
    
    def enable(self,timestep:int) -> None :
        self.__ds0_sensor.enable(timestep)
        self.__ds1_sensor.enable(timestep)
        self.__ds10_sensor.enable(timestep)
        self.__ds2_sensor.enable(timestep)
        self.__ds3_sensor.enable(timestep)
        self.__ds4_sensor.enable(timestep)
        self.__ds5_sensor.enable(timestep)
        self.__ds6_sensor.enable(timestep)
        self.__ds7_sensor.enable(timestep)
        self.__ds8_sensor.enable(timestep)
        self.__ds9_sensor.enable(timestep)
        self.__us0_sensor.enable(timestep)
        self.__us1_sensor.enable(timestep)
        self.__us2_sensor.enable(timestep)
        self.__us3_sensor.enable(timestep)
        self.__us4_sensor.enable(timestep)

    def getDistanceValue(self):
        return [self.__ds0_sensor.getValue(),self.__ds1_sensor.getValue()]
        #return self.__ds1_sensor.getValue()

class FugitiveRobotGPS():

    def __init__(self):
        self.__gps = GPS('gps')
    
    def enable(self,timestep:int) -> None :
        self.__gps.enable(timestep)

    def getCoordinates(self):
        return self.__gps.getCoordinateSystem()

robot = FugitiveRobot()
timestep = int(robot.getBasicTimeStep())

while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:

    #val = robot.distances.getDistanceValue()
    #val = robot.distance_detection() 

    val = robot.coordinates(timestep)
    print(val)
    #robot.run()

