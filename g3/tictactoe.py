import pygame, sys

pygame.init()

WIDTH, HEIGHT = 800, 800

FONT = pygame.font.Font("assets/Roboto-Regular.ttf", 50)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

BOARD = pygame.image.load("assets/Board.png")
X_IMG = pygame.image.load("assets/X.png")
O_IMG = pygame.image.load("assets/O.png")

BG_COLOR = (214, 201, 227)

board = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
graphics_board = [[[None, None], [None, None],[None, None]],
                  [[None, None], [None, None],[None, None]],
                  [[None, None], [None, None],[None, None]]]

to_move = 'X'

screen.fill(BG_COLOR)
screen.blit(BOARD, (16, 8))


def add_XO(board, graphical_board, to_move):
    current_pos =  pygame.mouse.get_pos()
    conv_x = (current_pos[0] - 65 )/ 835 * 2
    conv_y = current_pos[1]/ 835 * 2

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()