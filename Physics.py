from Vector2D import Vector2D
class Physics:
    def __init__(self, mass, static_friction, kinetic_friction, velocity):
        self.mass = mass
        self.static_friction = static_friction
        self.kinetic_friction = kinetic_friction
        self.inverse_mass = 1/mass
        self.force_this_frame = Vector2D(0, 0)
        self.velocity = velocity

    def add_force(self, force):
        self.force_this_frame += force

    def clear_force(self):
        self.force_this_frame = Vector2D(0, 0)

    def apply_force(self, timestep, body):
        self.velocity += self.inverse_mass*self.force_this_frame*timestep
        body.position += self.velocity * timestep
        self.force_this_frame = Vector2D(0, 0)

    def add_friction(self):
        self.add_force(-self.velocity*self.kinetic_friction)
