from abc import ABC, abstractmethod

class SmartHome(ABC):
    @abstractmethod
    def setProperties(self, **kwargs):
        pass
    @abstractmethod
    def getProperties(self, **kwargs):
        pass


class Lights(SmartHome):
    def setProperties(self, name, room, type_of_light, luminosity, color):
        self.name = name
        self.room = room
        self.type_of_light = type_of_light
        self.luminosity = luminosity
        self.color = color

    def getProperties(self):
        return f"Light Name: {self.name}, Room: {self.room}, Type: {self.type_of_light}, Luminosity: {self.luminosity} lumens, Color: {self.color}"
    
    def __str__(self):
        return self.getProperties()


class Routers(SmartHome):
    def setProperties(self, name, room, IP, supported_frequencies, mesh):
        self.name = name
        self.room = room
        self.IP = IP
        self.supported_frequencies = supported_frequencies
        self.mesh = mesh

    def getProperties(self):
        return f"Router Name: {self.name}, Room: {self.room}, IP: {self.IP}, Supported Frequencies: {self.supported_frequencies}, Mesh: {self.mesh}"
    
    def __str__(self):
        return self.getProperties()

light = Lights()
light.setProperties("Stropní", "Obývák", "LED", 800, "bílá")
print(light)

router = Routers()
router.setProperties("TP-Link Archer", "Kancelář", "192.168.1.1", "2.4 GHz, 5 GHz", True)
print(router)