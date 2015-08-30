class health:
    def __init__(self):
        self.x = 1

class entity:
    def __init__(self):
        self.components = {}

    def get_component(self, component):
        return self.components.get(component)

class ship(entity):
    def __init__(self):
        super().__init__()
        self.components['health'] = health()

class controller:
    def __init__(self):
        self.health_components = []

    def add_health(self, ship):
        self.health_components.append(ship.get_component('health'))

a=ship()
b=ship()
c=controller()
c.add_health(a)
c.add_health(b)

print(c.health_components[0].x)
print(a.get_component('health').x)

c.health_components[0].x-=1
print(c.health_components[0].x)
print(a.get_component('health').x)
