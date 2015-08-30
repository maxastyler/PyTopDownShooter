from Vector2D import Vector2D
import Collider

class GameController:
    def __init__(self, SCREEN_SIZE):
        self.keys = []
        self.components_list = ['health', 'body', 'renderer', 'controller',
                               'ai', 'physics']
        self.components = {}
        for component in self.components_list:
            self.components[component] = {}
        self.collision_manifold = []

        self.SCREEN_SIZE = SCREEN_SIZE

        self.key_num = 0

    def print_entities(self):
        for component in self.components_list:
            print(component)
            for entity in self.components[component]:
                print(entity, self.components[component][entity])

    def add_entity(self, entity):
        self.keys.append(self.key_num)
        for component in self.components_list:
            if entity.has_component(component):
                self.components[component][self.key_num] = entity.get_component(component)
        self.key_num+=1
        return self.key_num-1

    def remove_entity(self, entity_key):
        for component in component_list:
            if entity_key in self.components[component]:
                self.components[component].pop(entity_key)

    def render(self, screen):
        for item in self.components['renderer']:
            self.components['renderer'][item].render(screen, self.components['body'][item])

    def collide(self):
        colliders_list = []
        for item in self.components['body']:
            if self.components['body'][item].collider==True:
                colliders_list.append(item)
        for i in range(len(colliders_list)):
            for j in range(i+1, len(colliders_list)):
                if i!=j:
                    i=colliders_list[i]
                    j=colliders_list[j]
                    penetration, normal = Collider.CircleCircleCollision.solve(self.components['body'][i], self.components['body'][j])
                    if penetration is not None and normal is not None:
                        restitution = min(self.components['body'][i].restitution, self.components['body'][j].restitution)
                        self.components['physics'][i].add_force(penetration*normal*restitution)
                        self.components['physics'][j].add_force(-penetration*normal*restitution)

    def collide_walls(self):
        for i in self.components['body']:
            if self.components['body'][i].collider:
                lx = self.components['body'][i].collider_radius+self.components['body'][i].position.x
                gx = self.components['body'][i].position.x-self.components['body'][i].collider_radius
                ly = self.components['body'][i].collider_radius+self.components['body'][i].position.y
                gy = self.components['body'][i].position.y-self.components['body'][i].collider_radius
                if lx < 0:
                    self.components['physics'][i].add_force(Vector2D(-lx, 0))
                if gx > self.SCREEN_SIZE[0]:
                    self.components['physics'][i].add_force(Vector2D(-(gx-self.SCREEN_SIZE[0]), 0))
                if ly < 0:
                    self.components['physics'][i].add_force(Vector2D(0, -ly))
                if gy > self.SCREEN_SIZE[1]:
                    self.components['physics'][i].add_force(Vector2D(0, -(gy-self.SCREEN_SIZE[1])))


    def control(self, key_input, mouse_input):
        for item in self.components['controller']:
            self.components['controller'][item].take_input(key_input, mouse_input, self.components['physics'][item])


    def apply_physics(self, timestep):
        for item in self.components['physics']:
            self.components['physics'][item].add_friction()
            self.components['physics'][item].apply_force(timestep, self.components['body'][item])
        self.collision_manifold.clear()
