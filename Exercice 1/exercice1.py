class Robot():

   # __slots__ = ('name', 'power','speed') 

    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
        
    # Getter / Setter

    def get_battery_level(self):
        return self.__battery_level

    def set_battery_level(self, battery_level):
        self.__battery_level = battery_level

    def get_current_speed(self):
        return self.__current_speed

    def set_current_speed(self, current_speed):
        self.__current_speed = current_speed

    def get_power(self):
        return self.__power

    def set_power_on(self):
        print('Power ON')
        __power = True 

    def set_power_off(self):
        print('Power OFF')
        __power = False


r = Robot()

print(r.get_battery_level())
r.set_current_speed(50)
print(r.get_current_speed())
