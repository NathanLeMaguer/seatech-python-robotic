from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """

    __state = True

    def start(self):
          self.__state = True 
          self.start_vehicule()

    @abstractmethod
    def start_vehicule(self):
          pass

    def stop(self):
          self.__state = False
          self.stop_vehicule()

    @abstractmethod
    def stop_vehicule(self):
          pass

    @abstractmethod
    def move(self):

        raise Exception("A implémenter")

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

    def move(self):
         print("L'hélice tourne")

class UUV(UnmannedVehicle, UnderseaVehicle):
    """Unmanned Undersea Vehicle"""

    def start_vehicule(self):

         print("Démarrage du réacteur nucléaire ...")

    def stop_vehicule(self):

         print ("Arrêt du réacteur nucléaire ...")

    def move(self):
         print("L'hélice tourne et crée de la cavitation")

class UGV(UnmannedVehicle, GroundVehicle):
    
    def start_vehicule(self):

         print("Démarrage du moteur électrique ...")

    def stop_vehicule(self):

         print ("Arrêt du moteur électrique ...")

    def move(self):
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

