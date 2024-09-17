import pygame



# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pygame.draw.circle(screen, "white", self.position, self.radius, 2 )

    def update(self, dt):
        # must override
        self.position += (self.velocity * dt)

    def check_collisions(self, other_object):
        distance = self.position.distance_to(other_object.position)
        radius_sum = self.radius + other_object.radius
        if distance <= radius_sum:
            return True
        return False
       

        
