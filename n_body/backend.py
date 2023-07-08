import numpy as np


class Body:
    def __init__(self, mass, radius, position, velocity):
        self.mass = mass
        self.radius = radius
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.acceleration = np.zeros_like(self.position)
        self.selected = False


def update_acceleration(bodies):
    num_bodies = len(bodies)
    for i in range(num_bodies):
        body = bodies[i]

        body.acceleration = np.zeros_like(body.position)

        for j in range(num_bodies):
            if i != j:
                other_body = bodies[j]
                displacement = other_body.position - body.position
                distance = np.linalg.norm(displacement)
                direction = displacement / distance
                gravitational_force = (
                    direction * other_body.mass * distance ** -2
                )
                body.acceleration += gravitational_force / body.mass


def update_velocity(bodies, dt):
    for body in bodies:
        body.velocity += body.acceleration * dt


def update_position(bodies, dt):
    for body in bodies:
        body.position += body.velocity * dt


def handle_collisions(bodies):
    num_bodies = len(bodies)
    for i in range(num_bodies):
        body = bodies[i]
        for j in range(i + 1, num_bodies):
            other_body = bodies[j]
            displacement = other_body.position - body.position
            distance = np.linalg.norm(displacement)
            if distance < body.radius + other_body.radius:
                normal = displacement / distance

                relative_velocity = body.velocity - other_body.velocity
                normal_velocity = np.dot(relative_velocity, normal)
                if normal_velocity > 0:
                    continue

                restitution = 0.8  # Coefficient of restitution
                impulse_magnitude = -(1 + restitution) * normal_velocity
                impulse_magnitude /= (1 / body.mass + 1 / other_body.mass)

                impulse = impulse_magnitude * normal

                # Apply repulsive force
                repulsive_force = (body.radius + other_body.radius)
                body.position -= body.radius * repulsive_force * normal / body.mass
                other_body.position += other_body.radius * \
                    repulsive_force * normal / other_body.mass

                body.velocity += impulse / body.mass
                other_body.velocity -= impulse / other_body.mass


def update_bodies(bodies, dt):
    update_acceleration(bodies)
    update_velocity(bodies, dt)
    update_position(bodies, dt)
    handle_collisions(bodies)
