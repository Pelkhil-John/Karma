from pygame import font

WIDTH = 1380
HEIGHT = 690
FPS = 60
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 60
HAND_SIZE = 256
RIGHT_HAND_REST_POS = (WIDTH-HAND_SIZE, HEIGHT-HAND_SIZE)
LEFT_HAND_REST_POS = (0, HEIGHT-HAND_SIZE)
RENDER_DIST = 500
SCALE_FACTOR = 1/500
# energy_

FONT: font.Font

def settup():
    global FONT
    FONT = font.SysFont("Calibri", 50)
