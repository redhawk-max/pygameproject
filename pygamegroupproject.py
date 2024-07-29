import pygame
import random
import os
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroid Dodger")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
SPACESHIP_WIDTH = 50
SPACESHIP_HEIGHT = 50
ASTEROID_WIDTH = 50
ASTEROID_HEIGHT = 50
POWER_UP_WIDTH = 30
POWER_UP_HEIGHT = 30

spaceship_img = pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
spaceship_img = pygame.transform.scale(spaceship_img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
spaceship_img = pygame.transform.rotate(spaceship_img, 180)
asteroid_img = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
asteroid_img = pygame.transform.scale(asteroid_img, (ASTEROID_WIDTH, ASTEROID_HEIGHT))
power_up_img = pygame.image.load(os.path.join("Assets","power_block.gif"))
power_up_img = pygame.transform.scale(power_up_img, (POWER_UP_WIDTH, POWER_UP_HEIGHT))

def create_spaceship():
    spaceship = {
        "image": spaceship_img,
        "rect": spaceship_img.get_rect(centerx=SCREEN_WIDTH // 2, bottom=SCREEN_HEIGHT - 10),
        "speed": 5,
        "powered_up": False,
        "power_up_time": 0
    }
    return spaceship

def create_asteroid():
    asteroid = {
        "image": asteroid_img,
        "rect": asteroid_img.get_rect(x=random.randint(0, SCREEN_WIDTH - ASTEROID_WIDTH),
                                      y=random.randint(-100, -40)),
        "speed": random.randint(3, 8)
    }
    return asteroid
    
def create_power_up():
    power_up = {
        "image": power_up_img,
        "rect": power_up_img.get_rect(x=random.randint(0, SCREEN_WIDTH - POWER_UP_WIDTH),
                                      y=random.randint(-100, -40)),
        "speed": 3
    }
    return power_up
########################################################################################

def move_spaceship(spaceship, dx):
    spaceship["rect"].x += dx
    if spaceship["rect"].left < 0:
        spaceship["rect"].left = 0
    if spaceship["rect"].right > SCREEN_WIDTH:
        spaceship["rect"].right = SCREEN_WIDTH

def update_spaceship(spaceship):
    if spaceship["powered_up"]:
        current_time = pygame.time.get_ticks()
        if current_time - spaceship["power_up_time"] > 5000:  # Power-up lasts 5 seconds
            spaceship["speed"] = 5
            spaceship["powered_up"] = False

def update_asteroid(asteroid):
    asteroid["rect"].y += asteroid["speed"]
    if asteroid["rect"].top > SCREEN_HEIGHT:
        asteroid["rect"].x = random.randint(0, SCREEN_WIDTH - ASTEROID_WIDTH)
        asteroid["rect"].y = random.randint(-100, -40)
        asteroid["speed"] = random.randint(3, 8)

def update_power_up(power_up):
    power_up["rect"].y += power_up["speed"]
    if power_up["rect"].top > SCREEN_HEIGHT:
        power_up["rect"].x = random.randint(0, SCREEN_WIDTH - POWER_UP_WIDTH)
        power_up["rect"].y = random.randint(-100, -40)

def draw_entity(entity, surface):
    surface.blit(entity["image"], entity["rect"].topleft)

# Main game function
def main():
    clock = pygame.time.Clock()
    running = True
    spaceship = create_spaceship()
    asteroids = [create_asteroid() for _ in range(5)]
    power_ups = [create_power_up() for _ in range(2)]
    score = 0
    font = pygame.font.SysFont(None, 36)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx = 0
        if keys[pygame.K_LEFT]:
            dx = -spaceship["speed"]
        if keys[pygame.K_RIGHT]:
            dx = spaceship["speed"]

        move_spaceship(spaceship, dx)
        update_spaceship(spaceship)

        for asteroid in asteroids:
            update_asteroid(asteroid)
            if spaceship["rect"].colliderect(asteroid["rect"]):
                running = False

        for power_up in power_ups:
            update_power_up(power_up)
            if spaceship["rect"].colliderect(power_up["rect"]):
                spaceship["speed"] = 10  # Double the speed
                spaceship["powered_up"] = True
                spaceship["power_up_time"] = pygame.time.get_ticks()
                power_up["rect"].y = SCREEN_HEIGHT + 1  # Move the power-up off the screen

        screen.fill(BLACK)
        draw_entity(spaceship, screen)
        for asteroid in asteroids:
            draw_entity(asteroid, screen)
        for power_up in power_ups:
            draw_entity(power_up, screen)

        score += 1
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
