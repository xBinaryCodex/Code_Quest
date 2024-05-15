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
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

# Load Assets
background_image = pygame.image.load('path_to_your_image.jpg')
player_image = pygame.image.load('path_to_player_image.png')
item_images = {
    'diploma': pygame.image.load('path_to_diploma_image.png'),  # Update to actual path
    'certificate': pygame.image.load('path_to_certificate_image.png'),  # Update to actual path
    'award': pygame.image.load('path_to_award_image.png'),  # Update to actual path
    'scholarship': pygame.image.load('path_to_scholarship_image.png')  # Update to actual path
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

class Item(pygame.sprite.Sprite):
    def __init__(self, image, type, description, position):
        super().__init__()
        self.image = image
        self.type = type
        self.description = description
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.collected = False

    def collect(self):
        if not self.collected:
            global collected_items
            collected_items += 1
            self.collected = True
            collect_sound.play()  # Play sound effect when collected
            draw_info_box(f"Collected: {self.type} - {self.description}")
            self.kill()  # Remove the item from the game to simulate collection

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


def level_1():
    running = True
    player = Player()
    items = pygame.sprite.Group()
    items.add(Item(item_images['diploma'], 'Diploma', 'Bachelor of Science in Computer Science', (100, 150)))
    items.add(Item(item_images['certificate'], 'Certificate', 'Certified Python Developer', (200, 300)))
    items.add(Item(item_images['award'], 'Award', 'Dean\'s List for Academic Excellence', (300, 450)))
    items.add(Item(item_images['scholarship'], 'Scholarship', 'Recipient of the Tech Innovators Scholarship', (400, 200)))
    all_sprites = pygame.sprite.Group(player, items)

    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(keys)
        screen.blit(background_image, [0, 0])
        all_sprites.draw(screen)

        # Collision Detection
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
            draw_text('Start Game', menu_font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)
            draw_text('Exit', menu_font, GREY, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)
        else:
            draw_text('Start Game', menu_font, GREY, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)
            draw_text('Exit', menu_font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)

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
    player = Player()
    items = pygame.sprite.Group()
    clouds = BackgroundAnimation('path_to_clouds_image.png', -1)  # Example for clouds moving left to right
    all_sprites = pygame.sprite.Group(player, items, clouds)
    items.add(Item(item_images['diploma'], 'Diploma', (100, 150)))
    items.add(Item(item_images['certificate'], 'Certificate', (200, 300)))

    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update all sprites
        all_sprites.update(keys)

        # Draw everything
        screen.fill((0, 0, 0))  # Clear screen
        screen.blit(background_image, [0, 0])  # Draw background
        all_sprites.draw(screen)  # Draw all sprites
        draw_progress()  # Update progress display

        # Collision Detection and Collection
        collisions = pygame.sprite.spritecollide(player, items, False)
        for collision in collisions:
            collision.collect()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


# Start the game
if __name__ == "__main__":
    main_menu()
