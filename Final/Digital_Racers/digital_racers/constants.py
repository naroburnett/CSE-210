import pygame
pygame.font.init()

# ----------------------------------------------------------------------------------------------
# GENERAL UTILITY METHODS
# ----------------------------------------------------------------------------------------------

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


def blit_text_center(win, font, text):
    render = font.render(text, 1, (200, 200, 200))
    win.blit(render, (win.get_width()/2 - render.get_width() /
                      2, win.get_height()/2 - render.get_height()/2))


# ----------------------------------------------------------------------------------------------
# GENERAL GAME CONSTANTS
# ----------------------------------------------------------------------------------------------

TRACK = scale_image(pygame.image.load("digital_racers/assets\images/race_track.png"), 0.9)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Racers")

MAIN_FONT = pygame.font.SysFont("comicsans", 30)

FPS = 60

START_VEL_BOT = 2
START_ROTATION_BOT = 4

level_list = ['Option 1: Race Track Speed Way','Option 2: Water Way']

MAX_VEL = 4
MAX_ROTATION = 4