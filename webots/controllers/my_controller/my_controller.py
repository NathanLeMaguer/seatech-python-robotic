"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor

class FugitiveRobot(Robot):
    def __init__(self):
         super().__init__()
         self.__motors = FugitiveRobotMotors()

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
        self.__right_wheel_motor.setVelocity(-5)

    def go_front_fast(self):
        self.__left_wheel_motor.setVelocity(25)
        self.__right_wheel_motor.setVelocity(25)

# create the Robot instance.
robot = FugitiveRobot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    robot.run()

# Enter here exit cleanup code.
