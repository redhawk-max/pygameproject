import pygame
import random
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("enemy Dodger")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
SPACESHIP_WIDTH = 50
SPACESHIP_HEIGHT = 50
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
POWER_UP_WIDTH = 30
POWER_UP_HEIGHT = 30

background_img = pygame.image.load(os.path.join("Assets", "space.png"))
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
spaceship_img = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
spaceship_img = pygame.transform.scale(spaceship_img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
spaceship_img = pygame.transform.rotate(spaceship_img, 180)
enemy_img = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
enemy_img = pygame.transform.scale(enemy_img, (ENEMY_WIDTH, ENEMY_HEIGHT))
power_up_img = pygame.image.load(os.path.join("Assets", "power_block.gif"))
power_up_img = pygame.transform.scale(power_up_img, (POWER_UP_WIDTH, POWER_UP_HEIGHT))

# ****************************************************** #
# The create_whatever function just returns a dictionary #
# of the "whatever"'s properties, same as assigning diff #
# variables for a single "whatever", except more compact #
def create_spaceship():
    spaceship = {
        "image": spaceship_img,
        "rect": spaceship_img.get_rect(centerx=SCREEN_WIDTH // 2, bottom=SCREEN_HEIGHT - 10),
        "speed": 5,
        "powered_up": False,
        "power_up_time": 0,
        "power_up_duration": 3000
    }
    return spaceship

def create_enemy():
    enemy = {
        "image": enemy_img,
        "rect": enemy_img.get_rect(x=random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH),
                                      y=random.randint(-100, -40)),
        "speed": random.randint(3, 8)
    }
    return enemy

def create_power_up():
    power_up = {
        "image": power_up_img,
        "rect": power_up_img.get_rect(x=random.randint(0, SCREEN_WIDTH - POWER_UP_WIDTH),
                                      y=random.randint(-100, -40)),
        "speed": 3
    }
    return power_up


# This is a function to make the spaceship move on the x axis only
# & to make the spaceship stay within the bound of the screen's width
def spaceship_movement(spaceship, i): 
    spaceship["rect"].x += i
    if spaceship["rect"].left < 0:
        spaceship["rect"].left = 0
    if spaceship["rect"].right > SCREEN_WIDTH:
        spaceship["rect"].right = SCREEN_WIDTH

# This is a function to make the changes on spaceship 
# When it touches the power_up
def update_spaceship(spaceship):
    if spaceship["powered_up"]:
        current_time = pygame.time.get_ticks()
        if current_time - spaceship["power_up_time"] > spaceship["power_up_duration"]:
            spaceship["speed"] = 5
            spaceship["powered_up"] = False

# This is a function to make the changes on enemy spaceship 
def update_enemy(enemy):
    enemy["rect"].y += enemy["speed"]
    if enemy["rect"].top > SCREEN_HEIGHT:
        enemy["rect"].x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
        enemy["rect"].y = random.randint(-100, -40)
        enemy["speed"] = random.randint(3, 8)

# Function to update the power-up
def update_power_up(power_up):
    power_up["rect"].y += power_up["speed"]
    if power_up["rect"].top > SCREEN_HEIGHT:
        power_up["rect"].x = random.randint(0, SCREEN_WIDTH - POWER_UP_WIDTH)
        power_up["rect"].y = random.randint(-100, -40)

# Function to draw an entity
def draw_entity(entity, surface):
    surface.blit(entity["image"], entity["rect"].topleft)

# Function to draw the power-up timer
def draw_power_up_timer(surface, spaceship, font):
    if spaceship["powered_up"]:
        current_time = pygame.time.get_ticks()
        remaining_time = max(0, spaceship["power_up_duration"] - (current_time - spaceship["power_up_time"]))
        timer_text = font.render(f"Power-up: {remaining_time / 1000:.1f}s", True, WHITE)
        surface.blit(timer_text, (SCREEN_WIDTH - 200, 10))

# Function to draw the defeat message and reset the game state
def draw_defeat(surface, font):
    defeat_text = font.render("DEFEAT", True, WHITE)
    surface.blit(defeat_text, (SCREEN_WIDTH // 2 - defeat_text.get_width() // 2, SCREEN_HEIGHT // 2 - defeat_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(3000)
    return True

def main():
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Times New Roman", 36)
    running = True

    while running:
        spaceship = create_spaceship()
        enemys = [create_enemy() for _ in range(5)]
        power_ups = [create_power_up() for _ in range(2)]
        score = 0

        game_over = False

        while not game_over:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = True

            keys = pygame.key.get_pressed()
            dx = 0
            if keys[pygame.K_LEFT]:
                dx = -spaceship["speed"]
            if keys[pygame.K_RIGHT]:
                dx = spaceship["speed"]

            spaceship_movement(spaceship, dx)
            update_spaceship(spaceship)

            for enemy in enemys:
                update_enemy(enemy)
                if spaceship["rect"].colliderect(enemy["rect"]):
                    game_over = draw_defeat(SCREEN, font)

            for power_up in power_ups:
                update_power_up(power_up)
                if spaceship["rect"].colliderect(power_up["rect"]):
                    spaceship["speed"] = 10  # Double the speed
                    spaceship["powered_up"] = True
                    spaceship["power_up_time"] = pygame.time.get_ticks()
                    power_up["rect"].y = SCREEN_HEIGHT + 1  # Move the power-up off the screen

            SCREEN.fill(BLACK)
            draw_entity(spaceship, SCREEN)
            for enemy in enemys:
                draw_entity(enemy, SCREEN)
            for power_up in power_ups:
                draw_entity(power_up, SCREEN)

            score += 1
            score_text = font.render(f"Score: {score}", True, WHITE)
            SCREEN.blit(score_text, (10, 10))

            draw_power_up_timer(SCREEN, spaceship, font)
            pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
