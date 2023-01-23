"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor

#Needed informations : 

# https://cyberbotics.com/doc/guide/tutorial-4-more-about-controllers?tab-language=python -> Lesson
# https://cyberbotics.com/doc/guide/khepera3 -> Robot parameters 

from controller import Robot, Motor, DistanceSensor

class FugitiveRobot(Robot):
    def __init__(self):
         super().__init__()
         self.__motors = FugitiveRobotMotors()
         self.__distances = FugitiveRobotSensors()

    def run(self, backward=False, forward=False, left=False, right=False):
        if (forward == True) : 
            self.__motors.go_front()
        if(backward == True) : 
            self.__motors.go_back()
        if(left == True) : 
            self.__motors.go_left()
        if(right == True) : 
            self.__motors.go_right()
        else : 
            self.__motors.go_front_fast()

    def distance(self):

        self.__distances.getDistanceValue()

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

class FugitiveRobotSensor(DistanceSensor):
    def __init__(self, name=None):
        super().__init__(name)
    
class FugitiveRobotSensors():
    def __init__(self):
        self.__ds0_sensor = FugitiveRobotSensor('ds0')
        self.__ds1_sensor = FugitiveRobotSensor('ds1')
        
    def getDistanceValue(self):
        #return [self.__ds0_sensor.getValue(),self.__ds1_sensor]
        return self.__ds1_sensor.getValue()

robot = FugitiveRobot()

timestep = int(robot.getBasicTimeStep())

while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    val = robot.distance()
    print(val)
    #robot.run()

# Enter here exit cleanup code.
