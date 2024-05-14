import pygame
import sys


# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
FPS = 30
WHITE = (255, 0, 0)
GREY = (50, 50, 50)
BLUE = (50, 50, 255)

# Load assets
background_image = pygame.image.load('images/Code_Quest_Cover.png')
player_image = pygame.image.load('path_to_player_image.png')  # Replace with the path to your player sprite
item_images = {
    'diploma': pygame.image.load('path_to_diploma_image.png'),  # Replace with path to diploma sprite
    'certificate': pygame.image.load('path_to_certificate_image.png')  # Replace with path to certificate sprite
}

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Code Quest - Portfolio Game")

# Setup clock
clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def draw_info_box(text):
    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    pygame.draw.rect(screen, BLUE, text_rect.inflate(20, 20))  # Draw a blue background slightly larger than the text
    screen.blit(text_surface, text_rect)  # Draw the text


# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Item Class
class Item(pygame.sprite.Sprite):
    def __init__(self, image, type, position):
        super().__init__()
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.collected = False

    def collect(self): 
        if not self.collected:
            self.collected = True
            draw_info_box(f"Collected: {self.type} - Detail about this item.")  # Enhanced display method
            self.kill()  # Remove the item from the game to simulate collection

# Level 1: Education and Certifications
def level_1():
    running = True
    player = Player()
    items = pygame.sprite.Group()
    items.add(Item(item_images['diploma'], 'Diploma', (100, 150)))
    items.add(Item(item_images['certificate'], 'Certificate', (200, 300)))
    all_sprites = pygame.sprite.Group(player, items)

    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(keys)
        screen.blit(background_image, [0, 0])
        all_sprites.draw(screen)

        # collisions detection
        collisions = pygame.sprite.spritecollide(player, items, False)
        for collision in collisions:
            collision.collect()  # Call the collect method when colliding with an item

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

def main_menu():
    menu_font = pygame.font.Font(None, 36)
    selected_item = 1

    while True:
        screen.blit(background_image, [0, 0])  # Draw the background image

        if selected_item == 1:
            draw_text('Start Game', menu_font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)
            draw_text('Exit', menu_font, GREY, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)
        else:
            draw_text('Start Game', menu_font, GREY, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)
            draw_text('Exit', menu_font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    selected_item = 2 if selected_item == 1 else 1
                if event.key == pygame.K_RETURN:
                    if selected_item == 1:
                        game_loop()
                    elif selected_item == 2:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()
        clock.tick(FPS)

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, [0, 0])  # Keep drawing the background in the game loop
        draw_text('Game Screen - Under Construction', pygame.font.Font(None, 36), WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Start the game
if __name__ == "__main__":
    main_menu()
