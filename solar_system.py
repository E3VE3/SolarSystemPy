import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)

# Font for labels
font = pygame.font.SysFont("Arial", 16)

# Sun (center of the screen)
SUN_X, SUN_Y = WIDTH // 2, HEIGHT // 2

class Planet:
    def __init__(self, name, distance, radius, color, speed):
        self.name = name
        self.distance = distance      # Distance from Sun (pixels)
        self.radius = radius          # Planet size (pixels)
        self.color = color
        self.speed = speed            # Orbital speed
        self.angle = 0                # Current angle (radians)
        self.x = SUN_X
        self.y = SUN_Y
    
    def orbit(self):
        """Update planet position around the Sun"""
        self.angle += self.speed
        self.x = SUN_X + math.cos(self.angle) * self.distance
        self.y = SUN_Y + math.sin(self.angle) * self.distance
    
    def draw(self, screen):
        """Draw the planet and its orbit path"""
        # Draw orbit path (circle)
        pygame.draw.circle(screen, (50, 50, 50), (SUN_X, SUN_Y), self.distance, 1)
        # Draw planet
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        # Draw name
        label = font.render(self.name, True, WHITE)
        screen.blit(label, (int(self.x) + self.radius + 5, int(self.y) - 10))

# Create planets (scaled distances and speeds for visualization)
planets = [
    Planet("Mercury", 50, 4, GRAY, 0.05),
    Planet("Venus", 80, 6, ORANGE, 0.035),
    Planet("Earth", 110, 7, BLUE, 0.03),
    Planet("Mars", 150, 5, RED, 0.024),
    Planet("Jupiter", 220, 14, ORANGE, 0.013),
    Planet("Saturn", 280, 12, (210, 180, 140), 0.009),
    Planet("Uranus", 340, 9, (173, 216, 230), 0.006),
    Planet("Neptune", 390, 8, (65, 105, 225), 0.005),
]

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # 60 FPS
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the Sun
    pygame.draw.circle(screen, YELLOW, (SUN_X, SUN_Y), 20)
    sun_label = font.render("Sun", True, YELLOW)
    screen.blit(sun_label, (SUN_X - 15, SUN_Y + 25))
    
    # Update and draw each planet
    for planet in planets:
        planet.orbit()
        planet.draw(screen)
    
    pygame.display.flip()

pygame.quit()