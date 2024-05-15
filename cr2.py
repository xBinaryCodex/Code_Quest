import pygame
import sys

# Initialize Pygame and Mixer for Sound
pygame.init()
pygame.mixer.init()

# Load Sound Effects and Music
background_music = pygame.mixer.music.load('path_to_background_music.mp3')
collect_sound = pygame.mixer.Sound('path_to_collect_sound.wav')
pygame.mixer.music.play(-1)  # Loop background music indefinitely

# Game Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 30

# Load Assets
background_image = pygame.image.load('path_to_your_image.jpg')
player_image = pygame.image.load('path_to_player_image.png')
item_images = {
    'diploma': pygame.image.load('path_to_diploma_image.png'),
    'certificate': pygame.image.load('path_to_certificate_image.png')
}

# Setup Display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Code Quest - Portfolio Game")

# Setup Clock
clock = pygame.time.Clock()

# Progress Tracking
collected_items = 0
total_items = len(item_images)

def draw_progress():
    progress_text = f"Items Collected: {collected_items} / {total_items}"
    draw_text(progress_text, pygame.font.Font(None, 24), WHITE, screen, 650, 30)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self, keys):
        # Movement keys logic here

class Item(pygame.sprite.Sprite):
    def __init__(self, image, type, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def collect(self):
        global collected_items
        collected_items += 1
        collect_sound.play()  # Play sound effect when collected
        draw_info_box(f"Collected: {self.type}")
        self.kill()

# Background Animation (example: moving clouds)
class BackgroundAnimation(pygame.sprite.Sprite):
    def __init__(self, image, speed):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:  # Reset position if fully scrolled
            self.rect.left = SCREEN_WIDTH

# Game levels, interactions, etc., continue here...

