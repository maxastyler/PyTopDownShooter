class GameController:
    def __init__(self):
        self.keys = []
        self.components_list = ['health', 'body', 'renderer', 'controller',
                               'ai', 'physics', 'collider']
        self.components = {}
        for component in self.components_list:
            self.components[component] = {}

        self.key_num = 0

    def add_entity(self, entity):
        self.keys.append(self.key_num)
        for component in self.components_list:
            if entity.has_component(component):
                self.components[component][self.key_num] = entity.get_component(component)

        self.key_num+=1

    def remove_entity(self, entity_key):
        for component in component_list:
            if entity_key in self.components[component]:
                self.components[component].pop(entity_key)

    def render(self, screen):
        for item in self.components['renderer']:
            self.components['renderer'][item].render(screen, self.components['body'][item])
