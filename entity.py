from point import Point

class Entity:
    def __init__(self,name,position = None):
        self.setName(name)
        self.setPosition(position)
        

    def __str__(self):
        return '{"'+self.__class__.__name__+'": {"name": "' + self.name + '", "position": ' + str(self.position) +'}}'

    # setters
    def setName(self, name):
        if isinstance(name,str):
            self.name = name
        else:
            self.name = ""
            
    def setPosition(self, position):
        if isinstance(position,Point):
            self.position = position
        else:
            self.position = Point()

