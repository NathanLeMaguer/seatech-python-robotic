import time 

class Robot():

    __name = "<unnamed>"
    __current_speed = 0
    __battery_level = 0
    states = ['shutown', 'running']
    __state = states[0]
    move_flag = False 

    def __init__(self,name='Mathieu'):
        self.__name=name

    def __str__(self):
        return self.__name

    # Getter / Setter

    def power_on(self):
        self.__state = self.states[1]
        print("Power ON ...")

    def power_off(self):
        self.__state = self.states[0]
        print("Power OFF ...")
        self.stop()

    def get_state (self):
        return self.__state

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
        if(current_speed > 100 or current_speed < -100):
            raise Exception("Vitesse non comprise dans la gamme. La vitesse doit être comprise entre -100 et 100 kts")

        self.__current_speed = current_speed

    # Méthodes    

    def recharge(self,battery_level):

        if(battery_level < 0 or battery_level > 100):
            raise Exception("Niveau de charge souhaité incohérent")

        i = self.get_battery_level()
        
        for i in range(battery_level+1):
        
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

        if   (self.get_current_speed() > 0):
            self.set_current_speed(0) 
        return self.move_flag 


    def resume_state_robot(self):

        print("State : ",self.get_state())
        print("Name :",self.get_name())
        print("Battery level :",self.get_battery_level(),"%")
        print("Current speed :",self.get_current_speed(),"kts")

    def create_robot(self): 
        
        name = input("Choisir un nom: " )
        self.set_name(name)
        battery_level = input("Choisir niveau de batterie : ")
        self.set_battery_level(battery_level)

if __name__ == "__main__":

    r = Robot()
    r.set_name("Jean-Michelle")
    r.power_on()
    try : 
        r.recharge(-12)
    except Exception as error : 
        print(error)
        print("Tentative de recharge en cours ...")
        try : 
            r.recharge(35)
        except Exception as error2 : 
            print(error2)
            print("Arrêt tentative de recharge")

    r.move()

    try : 
        r.set_current_speed(-102)
    except Exception as error :
        print(error)
        print("Tentative de mofication vitesse en cours ...")
        try : 
            r.set_current_speed(75)
        except Exception as error2 : 
            print(error2)
            print("Arrêt tentative de modification de vitesse")     
        
    r.resume_state_robot()

    r.power_off()

    r2 = Robot()
    r2.create_robot()
    r2.resume_state_robot()

