class Entity:
    def __init__(self):
        self.components = {}

    def has_component(self, component):
        if component in self.components:
            return True
        return False

    def get_component(self, component):
        if self.has_component(component):
            return self.components.get(component)
        return None

    def add_component(self, component_name, component):
        if not self.has_component(component_name):
            self.components[component_name]=component

    def remove_component(self, component_name):
        if self.has_component(component_name):
            self.components.pop(component_name)
