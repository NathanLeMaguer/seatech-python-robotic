from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """

    __state = False

    def start(self):
          """
               Change bool variable state to True 
          """
          if(self.__state == False):
               self.__state = True 
               self.start_vehicule()
          else:
               print("Véhicule déjà démarré ...")

    @abstractmethod
    def start_vehicule(self):
          """
               Abstract method of Start
          """
          pass

    def stop(self):
          """
               Change bool variable state to False
          """
          if(self.__state == True):
               self.__state = False
               self.stop_vehicule()
          else:
               print("Véhicule déjà à l'arrêt ...")

    @abstractmethod
    def stop_vehicule(self):
          """
               Abstract method of Stop
          """
          pass

    def move(self):
          """
               Check possibility to move 
          """
          if(self.__state == True):
               self.move_vehicule()
          else:
               print("Véhicule à l'arrêt - Erreur")

    @abstractmethod
    def move_vehicule(self):
          """
               Abstract method of Move
          """
          pass

class AerialVehicle():
    """ A vehicle made for fly."""
    
    def fly(self):
        print("Le véhicule vole...")

class GroundVehicle():
    """ A vehicle made for ground fields."""

    def ride(self):
        print("Le véhicule roule ...")

class UnderseaVehicle():
    """ A vehicle made for sea."""

    def dive(self):
        print("Dilution dans l'Atlantique en cours ...")

class UAV(UnmannedVehicle, AerialVehicle):
    """Unmanned Aerial Vehicle"""
    
    def start_vehicule(self):

         print("Démarrage du moteur diesel ...")

    def stop_vehicule(self):

         print ("Arrêt du moteur diesel ...")

    def move_vehicule(self):
         print("L'hélice tourne")

class UUV(UnmannedVehicle, UnderseaVehicle):
    """Unmanned Undersea Vehicle"""

    def start_vehicule(self):

         print("Démarrage du réacteur nucléaire ...")

    def stop_vehicule(self):

         print ("Arrêt du réacteur nucléaire ...")

    def move_vehicule(self):
         print("L'hélice tourne et crée de la cavitation")

class UGV(UnmannedVehicle, GroundVehicle):
    
    def start_vehicule(self):

         print("Démarrage du moteur électrique ...")

    def stop_vehicule(self):

         print ("Arrêt du moteur électrique ...")

    def move_vehicule(self):
         print("Les roues tournent")

if __name__ == '__main__':

    uav = UAV()
    uav.start()
    uav.move()

    ugv = UGV()
    ugv.start()
    ugv.move()

    uuv = UUV()
    uuv.start()
    uuv.move() 

    help(UnmannedVehicle)