from entity import Entity, Point

a = Entity("object 1")

objects = [a, Entity("object 2"), Entity("object 3")]
for ob in objects:
    print ob
print 'selected: ', objects[1]

box = objects[1]

#remove
del objects[1]

for ob in objects:
    print ob

print 'in box: ', box
