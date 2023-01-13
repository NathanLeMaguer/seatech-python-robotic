from Robot import Robot 
#from fichier Robot.py import class Robot 

class Human():   
    
    __slots__ = (
        "__sexe",
        "__digestFlag"
    )

    def __init__(self,sexe):

        self.__sexes = ['male', 'female']
        self.__digestFlag = False

        if(not sexe):
            self.__sexe = self.__sexes[0]
        else:
            self.__sexe = sexe

    def __str__(self):
        return self.__sexe

    # Getter / Setter

    @property
    def sexe(self) -> list:
        return self.__sexe

    @property 
    def digestFlag(self) -> bool:
        return self.__digestFlag

    @sexe.setter 
    def sexe(self,sexe):
        self.__sexe = sexe

    @digestFlag.setter
    def digestFlag(self,digestFlag):
        self.__digestFlag=digestFlag

    # Méthodes

    def eat(self, food):
       
        if(self.digestFlag == True):
            print("J'ai déjà mangé, je suis repu !")
        else :

            if(type(food) == list):
                print(self.get_name(),'eat',' '.join(food))
            else : 
                print(self.get_name(),'eat',food)

            self.digestFlag = True 

    def digest(self):
        if(self.digestFlag == True):
            print("Digestion en cours veuillez patientez ... L'opération peut prendre quelques minutes ...")
            self.digestFlag = False 
        else:
            print("Aucun aliment à digérer !")
        


class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)

    def __str__(self):
        return Robot.__str__(self) + " is a " + Human.__str__(self)

if __name__ == "__main__":

    cyborg = Cyborg('Deux Ex Machina','male')
    cyborg.sexe = 'female'
    print(cyborg.get_name(), 'sexe', cyborg.sexe)
    cyborg.recharge(5)
    cyborg.resume_state_robot()
    cyborg.eat('banana')
    cyborg.eat(['coca', 'chips'])
    cyborg.digest()
    print(cyborg)