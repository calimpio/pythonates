from point import Point

class Entity:
    def __init__(self,name,point = None):
        if isinstance(name,str):
            self.name = name
        else:
            self.name = ""

        if isinstance(point,Point):
            self.position = point
        else:
            self.position = Point()

    def __str__(self):
        return '{"'+self.__class__.__name__+'": {"name": "' + self.name + '","position": ' + str(self.position) +'}}'
