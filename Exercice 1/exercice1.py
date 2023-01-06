import time 

class Robot():

   # __slots__ = ('name', 'power','speed') 

    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    move_flag = False 

    # Getter / Setter

    def get_name(self):
        return self.__name

    def set_name(self,name):
            self.__name = name

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

    def recharge(self,battery_level):

        i = self.get_battery_level()
        
        for i in range(battery_level+1):
        #for self.get_battery_level() < battery_level:
        
            self.set_battery_level(i)
            time.sleep(0.05)         
            print("Charge en cours : ",i,"%")

    def move(self):

        if(self.move_flag == False):
            print("Déplacement du robot en cours ...")
            self.move_flag = True
        else:
            print("Déplacement déjà en cours ...")

        if(self.get_current_speed() == 0):
            self.set_current_speed(50) 
        return self.move_flag 
    
    def stop(self):

        if(self.move_flag == True):
            print("Arrêt déplacement du robot ...")
            self.move_flag = False
        else:
            print("Robot déjà à l'arrêt ...")

        if(self.get_current_speed > 0):
            self.set_current_speed(0) 
        return self.move_flag 


    def resume_state_robot(self):

        print("Name :",self.get_name())
        print("Battery level :",self.get_battery_level(),"%")
        print("Vitesse de déplacement :",self.get_current_speed(),"kts")

r = Robot()

# print(r.get_battery_level())
# r.set_current_speed(50)
# print(r.get_current_speed())
# #r.recharge(50)
# #print("Fin de charge : ",r.get_battery_level(),"%")

# r.move()

r.recharge(35)
r.move()
r.resume_state_robot()
