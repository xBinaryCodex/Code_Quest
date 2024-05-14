import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Code Quest - Portfoliio Game")

# Setup clock
clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text('Main Menu', pygame.font.Font(None, 50), WHITE, screen, 300, 225)
        draw_text('1. Start Game', pygame.font.Font(None, 36), WHITE, screen, 310, 300)
        draw_text('2. Exit', pygame.font.Font(None, 36), WHITE, screen, 350, 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop()
                if event.key == pygame.K_2:
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
            
        screen.fill(BLACK)
        draw_text('Game Screen - Under Construction', pygame.font.Font(None, 36), WHITE, screen, 200, 300)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
# Start the game
if __name__ == "__main__":
    main_menu()
