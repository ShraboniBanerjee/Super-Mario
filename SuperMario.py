import pygame
import random

# Initialize Pygame
pygame.init()

# Game dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player dimensions
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

# Coin dimensions
COIN_WIDTH = 30
COIN_HEIGHT = 30

# Obstacle dimensions
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = 70

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blockchain Game")

# Load player image
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))

# Load coin image
coin_image = pygame.image.load("coin.png")
coin_image = pygame.transform.scale(coin_image, (COIN_WIDTH, COIN_HEIGHT))

# Load obstacle image
obstacle_image = pygame.image.load("obstacle.png")
obstacle_image = pygame.transform.scale(obstacle_image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

# Game clock
clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed = 5
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
    
    def draw(self):
        screen.blit(self.image, self.rect)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(100, 500)
        self.rect.y = random.randint(100, SCREEN_HEIGHT - 100)
        self.speed = 3
    
    def update(self):
        self.rect.x -= self.speed
    
    def draw(self):
        screen.blit(self.image, self.rect)

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = obstacle_image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(100, 500)
        self.rect.y = random.randint(100, SCREEN_HEIGHT - 100)
        self.speed = 3
    
    def update(self):
        self.rect.x -= self.speed
    
    def draw(self):
        screen.blit(self.image, self.rect)

# Create player object
player = Player()

# Sprite groups
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
all_sprites.add(player)

# Game loop
running = True
collected_coins = pygame.sprite.Group()  # Initialize collected coins as a sprite group
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update
    all_sprites.update()
    
    # Check collision with coins
    collected = pygame.sprite.spritecollide(player, coins, True)
    collected_coins.add(collected)  # Add collected coins to the sprite group
    
    # Check collision with obstacles
    collided_obstacles = pygame.sprite.spritecollide(player, obstacles, False)
    if collided_obstacles:
        running = False  # Game over
    
    # Spawn new coins
    if len(coins) < 5:
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
    
    # Spawn new obstacles
    if len(obstacles) < 3:
        new_obstacle = Obstacle()
        obstacles.add(new_obstacle)
        all_sprites.add(new_obstacle)
    
    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    # Display collected coins count
    font = pygame.font.Font(None, 30)
    coin_text = font.render("Coins: " + str(len(collected_coins)), True, WHITE)
    screen.blit(coin_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
