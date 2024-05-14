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
GREY = (100, 100, 100)

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Code Quest - Portfoliio Game")

# Setup clock
clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    menu_font = pygame.font.Font(None, 36)
    selected_item = 1

    while True:
        screen.fill(BLACK)

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

        screen.fill(BLACK)
        draw_text('Game Screen - Under Construction', pygame.font.Font(None, 36), WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Start the game
if __name__ == "__main__":
    main_menu()