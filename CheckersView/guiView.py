import sys
from CheckersModel.gameConstants import ROWS, COLS, BOARD_DIM
from CheckersView.ACheckersView import ACheckersView
import pygame


class GuiView(ACheckersView):
    """Handles viewing capabilities of checkers using Pygame as a basis for
    a graphical interface. Includes drawing board, pieces, indicating turn,
    score of game, as well as displaying the winner

    Args:
        dim : int - Dimension of the board to draw
        font : String - String containing a font to use for pygame
        font_size : int - Size to display font in for use with pygame"""

    def __init__(self, dim=BOARD_DIM, font='Comic Sans MS', font_size=18):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont(font, font_size)
        self.dim = dim
        self.screen = pygame.display.set_mode([dim, dim + 100])
        icon_file = open('C:/Users/pburn/Desktop/Projects/CheckersProject/CheckersView/checkers_icon.png')
        icon = pygame.image.load(icon_file)
        pygame.display.set_icon(icon)
        pygame.display.set_caption('AI Checkers')

    def show_board(self, board_string):
        """Draws the background of the checkers board. Does so utilizing the board
        dimensions supplied and pygame. Updates the pygame display once all drawings
        have been made"""

        pygame.event.pump()
        self.screen.fill((0, 0, 0))
        width = int(BOARD_DIM / ROWS)
        for row in range(1, ROWS + 1):
            for col in range(1, COLS + 1):
                x = width * row - width
                y = width * col - width
                x2 = width * row
                y2 = width * col
                if row % 2 == 0 and col % 2 == 0:
                    pygame.draw.rect(surface=self.screen, color=(255, 255, 255),
                                     rect=(x, y, x2, y2), width=0)
                elif row % 2 == 1 and col % 2 == 1:
                    pygame.draw.rect(surface=self.screen, color=(255, 255, 255),
                                     rect=(x, y, x2, y2), width=0)
                else:
                    pygame.draw.rect(surface=self.screen, color=(0, 0, 0),
                                     rect=(x, y, x2, y2), width=0)

        pygame.draw.rect(surface=self.screen, color=(128, 128, 128),
                         rect=(0, width * COLS, width * ROWS, width * COLS + width), width=0)

        pygame.display.update()

    def show_pieces(self, board_string):
        """Draws all of the checkers game states corresponding pieces. Gets information
        of the board which is supplied to the method. Updates the display after drawing.

        Args:
            board_string : String - String representation of the board state to draw"""

        pygame.event.pump()
        half_square = BOARD_DIM / ROWS / 2
        for row_idx, row in enumerate(board_string.split('\n')):
            for char_idx, char in enumerate(row.split()):
                center_x = (BOARD_DIM / ROWS) * char_idx + half_square
                center_y = (BOARD_DIM / COLS) * row_idx + half_square
                if char == 'W':
                    pygame.draw.circle(surface=self.screen, color=(255, 255, 255),
                                       center=(center_x, center_y), radius=half_square - 5)
                elif char == 'Wk':
                    pygame.draw.circle(surface=self.screen, color=(255, 255, 255),
                                       center=(center_x, center_y), radius=half_square - 5)
                    pygame.draw.circle(surface=self.screen, color=(212, 175, 55),
                                       center=(center_x, center_y), radius=half_square - 25)
                elif char == 'B':
                    pygame.draw.circle(surface=self.screen, color=(128, 128, 128),
                                       center=(center_x, center_y), radius=half_square - 5)
                elif char == 'Bk':
                    pygame.draw.circle(surface=self.screen, color=(128, 128, 128),
                                       center=(center_x, center_y), radius=half_square - 5)
                    pygame.draw.circle(surface=self.screen, color=(212, 175, 55),
                                       center=(center_x, center_y), radius=half_square - 25)

        pygame.display.update()

    def show_score(self, black, white, move):
        """Draws the remaining number of pieces as well as which players move it is.
        Does this by being supplied that information. Updates display after drawing
        score.

        Args:
            black : int - Remaining number of pieces for Black
            white : int - Remaining number of pieces for White
            move : bool - True if Blacks turn, False if Whites turn"""

        pygame.event.pump()
        pygame.draw.rect(surface=self.screen, color=(128, 128, 128),
                         rect=(0, BOARD_DIM, BOARD_DIM, BOARD_DIM + 75), width=0)

        # If black turn
        if move:
            score = self.font.render(f'White Pieces: {white}  '
                                     f'Black Pieces: {black}  '
                                     f'Move: Black', True, (255, 255, 255))
        # If white turn
        else:
            score = self.font.render(f'White Pieces: {white}  '
                                     f'Black Pieces: {black}  '
                                     f'Move: White', True, (255, 255, 255))

        self.screen.blit(score, (40, BOARD_DIM + 20))

        pygame.display.update()

    def show_winner(self, winner):
        """Displays the winner of the game using the supplied winner. Updates the
        display after drawing the winner.

        Args:
            winner : String - String representing winner of the game"""

        pygame.event.pump()
        size = int(BOARD_DIM / 2)
        offset = int(BOARD_DIM / ROWS)
        pygame.draw.rect(surface=self.screen, color=(128, 128, 128),
                         rect=(size - offset, size + offset, size - offset, size + offset), width=0)

        winner = self.font.render(f'{winner} Wins!', True, (255, 255, 255))
        self.screen.blit(winner, (size, size))

        pygame.display.update()

    def get_click(self):
        """Event listener using Pygame to get the move to be made by the player using
        mouse clicks. To begin the move, press down on a piece. Release the piece
        in the square you are trying to move to.

        Returns:
            move : (int, int, int, int) - Tuple of ints representing (row_from, col_from,
            row_to, col_to) form of a move"""

        down = None
        up = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close_view()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    down = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    up = pygame.mouse.get_pos()
                if down is not None and up is not None:
                    return down[0], down[1], up[0], up[1]

    def close_view(self):
        """Called to close the pygame window successfully"""
        pygame.quit()
        sys.exit()

    def prompt_user(self, black_move):
        super().prompt_user(black_move)

    def show_move(self, row_from, col_from, row_to, col_to):
        super().show_move(row_from, col_from, row_to, col_to)
