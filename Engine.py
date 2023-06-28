import pygame
import numpy as np

from game import Game


# Configuration settings
CELL_SIZE = 80
MARGIN = 5
WINDOW_WIDTH = CELL_SIZE * 8 + MARGIN
WINDOW_HEIGHT = CELL_SIZE * 8 + MARGIN

# Configure Colors
color = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "background": (136, 74, 57),
    "cell": (195, 129, 84),
    "cell-hover": (97, 64, 42),
    "cell-selected": (220, 154, 107),
    "cell-successful-move": (136, 247, 119),
    "cell-failed-move": (247, 119, 119),
    "cell-successful-move-hover": (68, 123, 59),
    "cell-failed-move-hover": (123, 59, 59)
}

game = Game()
board = game.board


def move(origin, destination):
    if origin == destination:
        return False
    global board, game
    if board[origin[1], origin[0]].move(destination):
        game.update_board(origin)
        board = game.board
        return True
    return False


if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    font = pygame.font.Font(None, 36)

    window.fill(color["background"])

    buttons = []
    for x in range(8):
        temp = []
        for y in range(8):
            temp.append(pygame.Rect(CELL_SIZE * x + MARGIN,
                                    CELL_SIZE * y + MARGIN,
                                    CELL_SIZE - MARGIN,
                                    CELL_SIZE - MARGIN))
        buttons.append(temp)

    origin = ()
    destination = ()
    failed_flg = False
    success_flg = False
    select_flg = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                failed_flg = False
                success_flg = False
                for x in range(8):
                    for y in range(8):
                        if buttons[x][y].collidepoint(event.pos):
                            if select_flg:
                                if board[origin[1], origin[0]] is not None:
                                    if move(origin, (x, y)):
                                        destination = (x, y)
                                        origin = ()
                                        success_flg = True
                                    else:
                                        failed_flg = True
                                        destination = ()
                                else:
                                    origin = ()
                                select_flg = False
                            else:
                                origin = (x, y)
                                select_flg = True

        for x in range(8):
            for y in range(8):
                if (x, y) == origin:
                    if failed_flg:
                        if buttons[x][y].collidepoint(pygame.mouse.get_pos()):
                            pygame.draw.rect(window, color["cell-failed-move-hover"], buttons[x][y])
                        else:
                            pygame.draw.rect(window, color["cell-failed-move"], buttons[x][y])
                    else:
                        pygame.draw.rect(window, color["cell-selected"], buttons[x][y])
                elif (x, y) == destination:
                    if success_flg:
                        if buttons[x][y].collidepoint(pygame.mouse.get_pos()):
                            pygame.draw.rect(window, color["cell-successful-move-hover"], buttons[x][y])
                        else:
                            pygame.draw.rect(window, color["cell-successful-move"], buttons[x][y])
                elif buttons[x][y].collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(window, color["cell-hover"], buttons[x][y])
                else:
                    pygame.draw.rect(window, color["cell"], buttons[x][y])
                if board[y, x] is not None:
                    text = font.render(str(board[y, x]), True, color[board[y, x].color])
                    text_rect = text.get_rect(center=buttons[x][y].center)
                    window.blit(text, text_rect)

        pygame.display.flip()

    pygame.quit()
