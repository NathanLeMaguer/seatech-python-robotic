class Robot():

    __slots__ = ('name', 'power','speed') 

    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
        
    # Getter / Setter

    def get_battery_level(self):
        return self.__battery_level

    def set_battery_level(self):
        self.__battery_level = 2

r = Robot()

print(r.get_battery_level())