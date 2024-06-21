import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Pac-Man class
class PacMan:
    def __init__(self):
        self.x = GRID_SIZE
        self.y = GRID_SIZE
        self.dx = 0
        self.dy = 0
        self.size = GRID_SIZE
        self.color = YELLOW

    def move(self, walls):
        new_x = self.x + self.dx * GRID_SIZE
        new_y = self.y + self.dy * GRID_SIZE
        if not (new_x, new_y) in walls:
            self.x = new_x
            self.y = new_y

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size // 2)

# Dot class
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = GRID_SIZE // 4
        self.color = WHITE

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

# Wall class
class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = GRID_SIZE
        self.color = BLUE

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

# Ghost class
class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = GRID_SIZE
        self.color = RED
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])

    def move(self, walls):
        new_x = self.x + self.dx * GRID_SIZE
        new_y = self.y + self.dy * GRID_SIZE
        if (new_x, new_y) in walls:
            self.dx = random.choice([-1, 1])
            self.dy = random.choice([-1, 1])
        else:
            self.x = new_x
            self.y = new_y

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

# Create game elements
pacman = PacMan()
dots = [Dot(x * GRID_SIZE, y * GRID_SIZE) for x in range(1, SCREEN_WIDTH // GRID_SIZE - 1) for y in range(1, SCREEN_HEIGHT // GRID_SIZE - 1)]
walls = [(x * GRID_SIZE, y * GRID_SIZE) for x in range(0, SCREEN_WIDTH // GRID_SIZE) for y in range(0, SCREEN_HEIGHT // GRID_SIZE) if x == 0 or y == 0 or x == SCREEN_WIDTH // GRID_SIZE - 1 or y == SCREEN_HEIGHT // GRID_SIZE - 1]
walls.extend([(5 * GRID_SIZE, y * GRID_SIZE) for y in range(5, 15)])
ghosts = [Ghost(GRID_SIZE * 10, GRID_SIZE * 10)]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman.dx = -1
                pacman.dy = 0
            elif event.key == pygame.K_RIGHT:
                pacman.dx = 1
                pacman.dy = 0
            elif event.key == pygame.K_UP:
                pacman.dx = 0
                pacman.dy = -1
            elif event.key == pygame.K_DOWN:
                pacman.dx = 0
                pacman.dy = 1

    pacman.move(walls)

    for ghost in ghosts:
        ghost.move(walls)

    # Check for collisions with dots
    for dot in dots[:]:
        if pacman.x == dot.x and pacman.y == dot.y:
            dots.remove(dot)
            break

    # Check for collisions with ghosts
    for ghost in ghosts:
        if pacman.x == ghost.x and pacman.y == ghost.y:
            running = False  # End the game if Pac-Man collides with a ghost

    # Clear the screen
    screen.fill(BLACK)

    # Draw Pac-Man, walls, dots, and ghosts
    pacman.draw()
    for wall in walls:
        Wall(wall[0], wall[1]).draw()
    for dot in dots:
        dot.draw()
    for ghost in ghosts:
        ghost.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(10)

# Quit Pygame
pygame.quit()