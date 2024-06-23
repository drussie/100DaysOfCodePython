import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
DARK_BLUE = (0, 0, 139)

# Game objects
WALL = 'W'
DOT = '.'
EMPTY = ' '
PACMAN = 'P'
GHOST = 'G'
POWER_PILL = 'O'

# Define the level layout
level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W............WW............W",
    "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
    "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
    "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
    "W..........................W",
    "W.WWWW.WW.WWWWWWWW.WW.WWWW.W",
    "W.WWWW.WW.WWWWWWWW.WW.WWWW.W",
    "W......WW....WW....WW......W",
    "WWWWWW.WWWWW WW WWWWW.WWWWWW",
    "WWWWWW.WWWWW WW WWWWW.WWWWWW",
    "WWWWWW.WW          WW.WWWWWW",
    "WWWWWW.WW WWWWWWWW WW.WWWWWW",
    "WWWWWW.WW W      W WW.WWWWWW",
    "W.......W W      W W...... W",
    "WWWWWW.WW W      W WW.WWWWWW",
    "WWWWWW.WW WWWWWWWW WW.WWWWWW",
    "WWWWWW.WW          WW.WWWWWW",
    "WWWWWW.WW WWWWWWWW WW.WWWWWW",
    "WWWWWW.WW WWWWWWWW WW.WWWWWW",
    "W............WW............W",
    "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
    "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
    "WO..WW................WW..OW",
    "WWW.WW.WW.WWWWWWWW.WW.WW.WWW",
    "WWW.WW.WW.WWWWWWWW.WW.WW.WWW",
    "W......WW....WW....WW......W",
    "W.WWWWWWWWWW.WW.WWWWWWWWWW.W",
    "W.WWWWWWWWWW.WW.WWWWWWWWWW.W",
    "W..........................W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]

# Ensure all rows have the same length
row_length = len(level[0])
for row in level:
    if len(row) != row_length:
        raise ValueError(f"All rows in the level must have the same length ({row_length}). Found row: {row}")

# Set up the game window
CELL_SIZE = 20
ROWS = len(level)
COLS = len(level[0])
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman - First Level")

# Pacman properties
pacman_x = COLS // 2
pacman_y = ROWS - 7
pacman_direction = 0  # 0: right, 1: up, 2: left, 3: down
score = 0

# Ghost properties
ghosts = [
    {'color': RED},
    {'color': PINK},
    {'color': CYAN},
    {'color': ORANGE}
]

# Power pill properties
power_active = False
power_timer = 0
POWER_DURATION = 100  # Duration of power pill effect (in frames)

# Function to find a valid position for ghosts
def find_valid_position():
    while True:
        x = random.randint(1, COLS-2)
        y = random.randint(1, ROWS-2)
        if level[y][x] != WALL:
            return x, y

# Set initial positions for ghosts
for ghost in ghosts:
    ghost['x'], ghost['y'] = find_valid_position()

def draw_board():
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell == WALL:
                pygame.draw.rect(screen, BLUE, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == DOT:
                pygame.draw.circle(screen, WHITE, (x*CELL_SIZE + CELL_SIZE//2, y*CELL_SIZE + CELL_SIZE//2), 2)
            elif cell == POWER_PILL:
                pygame.draw.circle(screen, WHITE, (x*CELL_SIZE + CELL_SIZE//2, y*CELL_SIZE + CELL_SIZE//2), 7)

def draw_pacman():
    pygame.draw.circle(screen, YELLOW, (pacman_x*CELL_SIZE + CELL_SIZE//2, pacman_y*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//2)

def draw_ghosts():
    for ghost in ghosts:
        color = DARK_BLUE if power_active else ghost['color']
        pygame.draw.circle(screen, color, (ghost['x']*CELL_SIZE + CELL_SIZE//2, ghost['y']*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//2)

def draw_score():
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def draw_power_timer():
    if power_active:
        font = pygame.font.Font(None, 36)
        timer_text = font.render(f"Power: {power_timer}", True, WHITE)
        screen.blit(timer_text, (WIDTH - 150, 10))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move Pacman
    keys = pygame.key.get_pressed()
    new_x, new_y = pacman_x, pacman_y
    if keys[pygame.K_LEFT] and pacman_x > 0 and level[pacman_y][pacman_x-1] != WALL:
        new_x -= 1
        pacman_direction = 2
    elif keys[pygame.K_RIGHT] and pacman_x < COLS-1 and level[pacman_y][pacman_x+1] != WALL:
        new_x += 1
        pacman_direction = 0
    elif keys[pygame.K_UP] and pacman_y > 0 and level[pacman_y-1][pacman_x] != WALL:
        new_y -= 1
        pacman_direction = 1
    elif keys[pygame.K_DOWN] and pacman_y < ROWS-1 and level[pacman_y+1][pacman_x] != WALL:
        new_y += 1
        pacman_direction = 3

    # Update Pacman position if valid move
    if level[new_y][new_x] != WALL:
        pacman_x, pacman_y = new_x, new_y

    # Eat dots or power pills
    if level[pacman_y][pacman_x] == DOT:
        level[pacman_y] = level[pacman_y][:pacman_x] + EMPTY + level[pacman_y][pacman_x+1:]
        score += 10
    elif level[pacman_y][pacman_x] == POWER_PILL:
        level[pacman_y] = level[pacman_y][:pacman_x] + EMPTY + level[pacman_y][pacman_x+1:]
        power_active = True
        power_timer = POWER_DURATION
        score += 50

    # Move Ghosts (simple random movement)
    for ghost in ghosts:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        moved = False
        for dx, dy in directions:
            new_x, new_y = ghost['x'] + dx, ghost['y'] + dy
            if 0 <= new_x < COLS and 0 <= new_y < ROWS:
                if level[new_y][new_x] != WALL:
                    ghost['x'], ghost['y'] = new_x, new_y
                    moved = True
                    break
        if not moved:
            # If no valid move found, stay in place
            pass

    # Check for collisions with ghosts
    for ghost in ghosts:
        if ghost['x'] == pacman_x and ghost['y'] == pacman_y:
            if power_active:
                # Reset ghost position when eaten
                ghost['x'], ghost['y'] = find_valid_position()
                score += 100
            else:
                print("Game Over!")
                running = False

    # Update power pill timer
    if power_active:
        power_timer -= 1
        if power_timer <= 0:
            power_active = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw game objects
    draw_board()
    draw_pacman()
    draw_ghosts()
    draw_score()
    draw_power_timer()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(10)

# Quit the game
pygame.quit()
