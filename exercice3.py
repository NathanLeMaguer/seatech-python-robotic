from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """

    __state__ = True

    @abstractmethod
    def start(self):

         #self.__state__ = True 
         #print("Démarrage ...")
        pass

    @abstractmethod
    def stop(self):

         #self.__state__ = False
         #print ("Arrêt ...")
        pass

    @abstractmethod
    def move(self):
         #print("Le véhicule avance")
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
    
    def start(self):

         self.__state__ = True 
         print("Démarrage du moteur diesel ...")

    def stop(self):

         self.__state__ = False
         print ("Arrêt du moteur diesel ...")

    def move(self):
         print("L'hélice tourne")

class UUV(UnmannedVehicle, UnderseaVehicle):
    """Unmanned Undersea Vehicle"""

    def start(self):

         self.__state__ = True 
         print("Démarrage du réacteur nucléaire ...")

    def stop(self):

         self.__state__ = False
         print ("Arrêt du réacteur nucléaire ...")

    def move(self):
         print("L'hélice tourne et crée de la cavitation")

class UGV(UnmannedVehicle, GroundVehicle):
    
    def start(self):

         self.__state__ = True 
         print("Démarrage du moteur électrique ...")

    def stop(self):

         self.__state__ = False
         print ("Arrêt du moteur électrique ...")

    def move(self):
         print("Les roues tournent")

if __name__ == '__main__':

    uav = UAV()
    uav.start()
    uav.move()

    # ugv = UGV()
    # ugv.do_something_interesting()
    # ugv.do_something_ground_specific()

    # uuv = UUV()
    # uuv.do_something_interesting()
    # uuv.do_something_undersea_specific() 