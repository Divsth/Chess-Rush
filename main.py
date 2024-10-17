# Import pygame module
import pygame
# Import random
import random
import asyncio



# Initialize pygame
pygame.init()

pygame.mixer.init()

music = pygame.mixer.music.load("sources/backgroundmusic.wav")

sfx = pygame.mixer.Sound("sources/move.wav")

# Define colors
BLACK = (63, 63, 63)
WHITE = (191, 191, 191) 
PURE_WHITE = (255, 255, 255)
PURE_BLACK = (0, 0 ,0)
#BROWN = (139, 69, 19)

# Define some color schemes for the board
color_schemes = [
    # Black and white
    (BLACK, WHITE),
    # Red and yellow
    ((255, 0, 0), (255, 255, 0)),
    # Green and blue
    (pygame.Color(0, 128, 0), pygame.Color(0, 0, 128)),
    # Purple and pink
    (pygame.Color("purple"), pygame.Color("pink")),
    # Orange and gray
    (pygame.Color(255, 165, 0), pygame.Color(108, 108, 108))
]


# Define color to string dictionary
color_dict = {(63, 63, 63): "black", (191, 191, 191): "white"}

# Define window size and title
WINDOW_SIZE = (640, 800)
WINDOW_TITLE = "Chess Rush"

# Create a window
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)

# Create a clock
clock = pygame.time.Clock()

# Define grid size and cell size
GRID_SIZE = 5
CELL_SIZE = WINDOW_SIZE[0] // GRID_SIZE

# Define turn (True for white, False for black)
turn = True

# Define game over flag
game_over = False

#Computer color
computer_color = BLACK

# Draw a horizontal line to separate the board from the text area 
pygame.draw.line(window, BLACK, (0, WINDOW_SIZE[0]), (WINDOW_SIZE[0], WINDOW_SIZE[0]), 5) 

# Define a function to draw a game over message on the window
def draw_game_over(): # this isnt used anymore
    # Create a font object with size 128
    font = pygame.font.SysFont("impact", 128)

    # Create a text surface with the message
    text = font.render("Game Over", True, PURE_WHITE)

    # Get the size and position of the text surface
    text_width = text.get_width()
    text_height = text.get_height()
    text_x = (WINDOW_SIZE[0] - text_width) // 2
    text_y = (WINDOW_SIZE[1] - text_height) // 2

    # Draw the text surface on the window
    window.blit(text, (text_x, text_y))


class TitleScreen:

    def __init__(self):
        #self.title_font = pygame.font.SysFont("impact", 64)
        #self.title_text = self.title_font.render("Chess Rush", True, WHITE)

        self.title_image = pygame.image.load("sources/title_image.png")
        self.title_image = pygame.transform.scale(self.title_image, (WINDOW_SIZE[0], WINDOW_SIZE[0]))
        
        self.info_font = pygame.font.SysFont("impact", 32) 
        


        

        #self.title_rect = self.title_text.get_rect(center=(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/4))
         

    def draw(self):
        window.fill(PURE_BLACK)
        window.blit(self.title_image, (0, 0))
        #window.blit(self.title_text, self.title_rect)
        if (statistics.num_challenges_completed !=5):
            self.start_text = self.info_font.render("Click to start", True, WHITE)
            self.start_rect = self.start_text.get_rect(center=(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]*4/5))
            window.blit(self.start_text, self.start_rect)
        else:
            
            self.start_text = self.info_font.render("Click to play again", True, WHITE)
            self.start_rect = self.start_text.get_rect(center=(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]*4/5))
            window.blit(self.start_text, self.start_rect)


            statistics.end_draw()
            
            

            





class Statistics:
    def __init__(self):
        # Create a list of possible challenges # *
        self.challenges = ["No captures for 5 moves", "Pieces can move at most 1 square", "Only knights and bishops can move",  ] # *

        # Pick a random challenge from the list # *
        self.challenge = random.choice(self.challenges) # *

        self.num_challenges_completed = 0

        # Create a counter to keep track of how many moves have been made under the current challenge # *
        self.challenge_moves = 0 # *

        # Create a variable to store the total start time in milliseconds # *
        self.start_time = pygame.time.get_ticks() # *

        # Create a list to store the elapsed times for each game in milliseconds # *
        self.elapsed_times = [] # *

        # Create variables to store the total time and average time per challenge in seconds # *
        self.total_time = 0 # *
        self.average_time = 0 # *


        # Create a font object with size 18
        self.font = pygame.font.SysFont("impact", 18)

        self.total_time_rounded = "%.2f" % self.total_time
        self.average_time_rounded = "%.2f" % self.average_time

        # Create text surfaces for the challenge, the total time elapsed, and the average time per challenge # *
        self.challenge_text = self.font.render("Challenge: " + self.challenge, True, PURE_WHITE) # *
        self.total_time_text = self.font.render("Total time: " + self.total_time_rounded + " seconds", True, PURE_WHITE) # *
        self.average_time_text = self.font.render("Average time: " + self.average_time_rounded + " seconds", True, PURE_WHITE) # *  
        self.num_challenges_completed_text = self.font.render("Round " + str(self.num_challenges_completed +1) + " / 5", True, PURE_WHITE) # * 

        # Get the size and position of the text surfaces # *
        self.challenge_text_width = self.challenge_text.get_width() # *
        self.challenge_text_height = self.challenge_text.get_height() # *
        self.challenge_text_x = (WINDOW_SIZE[0] - self.challenge_text_width) // 2 # *
        self.challenge_text_y = WINDOW_SIZE[0] + 20 # *

        self.total_time_text_width = self.total_time_text.get_width() # *
        self.total_time_text_height = self.total_time_text.get_height() # *
        self.total_time_text_x = (WINDOW_SIZE[0] - self.total_time_text_width) // 2 # *
        self.total_time_text_y = WINDOW_SIZE[0] + 60 # *

        self.average_time_text_width = self.average_time_text.get_width() # *
        self.average_time_text_height = self.average_time_text.get_height() # *
        self.average_time_text_x = (WINDOW_SIZE[0] - self.average_time_text_width) // 2 # *
        self.average_time_text_y = WINDOW_SIZE[0] + 100 # *

        self.num_challenges_completed_text_width = self.num_challenges_completed_text.get_width() # *
        self.num_challenges_completed_text_height = self.num_challenges_completed_text.get_height() # *
        self.num_challenges_completed_text_x = (WINDOW_SIZE[0] - self.num_challenges_completed_text_width) // 2 # *
        self.num_challenges_completed_text_y = WINDOW_SIZE[0] + 140 # *


    def draw(self):
        # Draw the text surfaces on the window # *
        window.blit(self.challenge_text, (self.challenge_text_x, self.challenge_text_y)) # *
        window.blit(self.total_time_text, (self.total_time_text_x, self.total_time_text_y)) # *
        window.blit(self.average_time_text, (self.average_time_text_x, self.average_time_text_y)) # *
        window.blit(self.num_challenges_completed_text, (self.num_challenges_completed_text_x, self.num_challenges_completed_text_y)) # *
    def end_draw(self):
        window.blit(self.total_time_text, (self.total_time_text_x, self.total_time_text_y)) # *
        window.blit(self.average_time_text, (self.average_time_text_x, self.average_time_text_y)) # *


    def update(self):
            # Get the current time in milliseconds
            current_time = pygame.time.get_ticks ()

            self.total_time = (current_time - self.start_time) / 1000

            self.total_time_rounded = "%.2f" % self.total_time
            self.average_time_rounded = "%.2f" % self.average_time


            self.challenge_text = self.font.render("Challenge: " + self.challenge, True, PURE_WHITE) # *
            self.total_time_text = self.font.render("Total time: " + self.total_time_rounded + " seconds", True, PURE_WHITE) # *
            self.average_time_text = self.font.render("Average time: " + self.average_time_rounded + " seconds", True, PURE_WHITE) # *  
            self.num_challenges_completed_text = self.font.render("Round " + str(self.num_challenges_completed) + " / 5", True, PURE_WHITE) # * 

            # Get the size and position of the text surfaces # *
            self.challenge_text_width = self.challenge_text.get_width() # *
            self.challenge_text_height = self.challenge_text.get_height() # *
            self.challenge_text_x = (WINDOW_SIZE[0] - self.challenge_text_width) // 2 # *
            self.challenge_text_y = WINDOW_SIZE[0] + 20 # *

            self.total_time_text_width = self.total_time_text.get_width() # *
            self.total_time_text_height = self.total_time_text.get_height() # *
            self.total_time_text_x = (WINDOW_SIZE[0] - self.total_time_text_width) // 2 # *
            self.total_time_text_y = WINDOW_SIZE[0] + 60 # *

            self.average_time_text_width = self.average_time_text.get_width() # *
            self.average_time_text_height = self.average_time_text.get_height() # *
            self.average_time_text_x = (WINDOW_SIZE[0] - self.average_time_text_width) // 2 # *
            self.average_time_text_y = WINDOW_SIZE[0] + 100 # *

            self.num_challenges_completed_text_width = self.num_challenges_completed_text.get_width() # *
            self.num_challenges_completed_text_height = self.num_challenges_completed_text.get_height() # *
            self.num_challenges_completed_text_x = (WINDOW_SIZE[0] - self.num_challenges_completed_text_width) // 2 # *
            self.num_challenges_completed_text_y = WINDOW_SIZE[0] + 140 # *


    def handle_new_round(self):
        # Get the current time in milliseconds
        current_time = pygame.time.get_ticks ()    
        
        # Calculate the elapsed time for this game in seconds
        elapsed_time = (current_time - (self.start_time + sum(self.elapsed_times)*1000)) / 1000
        self.elapsed_times.append(elapsed_time)
        self.average_time = sum(self.elapsed_times) / len(self.elapsed_times)
        # Pick a new challenge from the list
        self.challenge = random.choice(self.challenges)

            
        self.challenge_moves = 0
    def reset(self): #literally the constructor
        # Create a list of possible challenges # *
        self.challenges = ["No captures for 5 moves", "Pieces can move at most 1 square", "Only knights and bishops can move",  ] # *

        # Pick a random challenge from the list # *
        self.challenge = random.choice(self.challenges) # *

        self.num_challenges_completed = 0

        # Create a counter to keep track of how many moves have been made under the current challenge # *
        self.challenge_moves = 0 # *

        # Create a variable to store the total start time in milliseconds # *
        self.start_time = pygame.time.get_ticks() # *

        # Create a list to store the elapsed times for each game in milliseconds # *
        self.elapsed_times = [] # *

        # Create variables to store the total time and average time per challenge in seconds # *
        self.total_time = 0 # *
        self.average_time = 0 # *


        # Create a font object with size 18
        self.font = pygame.font.SysFont("impact", 18)

        self.total_time_rounded = "%.2f" % self.total_time
        self.average_time_rounded = "%.2f" % self.average_time

        # Create text surfaces for the challenge, the total time elapsed, and the average time per challenge # *
        self.challenge_text = self.font.render("Challenge: " + self.challenge, True, PURE_WHITE) # *
        self.total_time_text = self.font.render("Total time: " + self.total_time_rounded + " seconds", True, PURE_WHITE) # *
        self.average_time_text = self.font.render("Average time: " + self.average_time_rounded + " seconds", True, PURE_WHITE) # *  
        self.num_challenges_completed_text = self.font.render("Round " + str(self.num_challenges_completed) + " / 5", True, PURE_WHITE) # * 

        # Get the size and position of the text surfaces # *
        self.challenge_text_width = self.challenge_text.get_width() # *
        self.challenge_text_height = self.challenge_text.get_height() # *
        self.challenge_text_x = (WINDOW_SIZE[0] - self.challenge_text_width) // 2 # *
        self.challenge_text_y = WINDOW_SIZE[0] + 20 # *

        self.total_time_text_width = self.total_time_text.get_width() # *
        self.total_time_text_height = self.total_time_text.get_height() # *
        self.total_time_text_x = (WINDOW_SIZE[0] - self.total_time_text_width) // 2 # *
        self.total_time_text_y = WINDOW_SIZE[0] + 60 # *

        self.average_time_text_width = self.average_time_text.get_width() # *
        self.average_time_text_height = self.average_time_text.get_height() # *
        self.average_time_text_x = (WINDOW_SIZE[0] - self.average_time_text_width) // 2 # *
        self.average_time_text_y = WINDOW_SIZE[0] + 100 # *

        self.num_challenges_completed_text_width = self.num_challenges_completed_text.get_width() # *
        self.num_challenges_completed_text_height = self.num_challenges_completed_text.get_height() # *
        self.num_challenges_completed_text_x = (WINDOW_SIZE[0] - self.num_challenges_completed_text_width) // 2 # *
        self.num_challenges_completed_text_y = WINDOW_SIZE[0] + 140 # *
           
            



# Define a class for the board
class Board:
    # Define the constructor
    def __init__(self):
        # Create an empty array for the board
        self.board = []

        # Loop through each row and column and fill the board with None values
        for row in range(GRID_SIZE):
            self.board.append([])
            for col in range(GRID_SIZE):
                self.board[row].append(None)

        # Create the pieces and place them on the board
        self.create_pieces()

    # Define a method to create the pieces and place them on the board
    def create_pieces(self):
        # Create the black pieces and place them on the first row
        self.board[0][0] = Rook(BLACK)
        self.board[0][1] = Knight(BLACK)
        self.board[0][2] = Bishop(BLACK)
        self.board[0][3] = Queen(BLACK)
        self.board[0][4] = King(BLACK)

        random.shuffle(self.board[0])

        # Create the white pieces and place them on the last row
        self.board[4][0] = King(WHITE)
        self.board[4][1] = Queen(WHITE)
        self.board[4][2] = Bishop(WHITE)
        self.board[4][3] = Knight(WHITE)
        self.board[4][4] = Rook(WHITE)

        random.shuffle(self.board[4])

    # Define a method to draw the board on the window
    def draw(self, color_scheme):
        # Loop through each row and column of the board
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                # Calculate the position and size of the cell
                x = col * CELL_SIZE
                y = row * CELL_SIZE
                w = CELL_SIZE
                h = CELL_SIZE

                # Draw the cell with alternating colors
                if (row + col) % 2 == 0:
                    color = color_scheme[0]
                else:
                    color = color_scheme[1]
                pygame.draw.rect(window, color, (x, y, w, h))

                # Draw the piece if it exists
                piece = self.board[row][col]
                if piece is not None:
                    piece.draw(x, y)

    # Define a method to get the piece at a given position
    def get_piece(self, row, col):
        # Check if the position is within the board
        if row >= 0 and row < GRID_SIZE and col >= 0 and col < GRID_SIZE:
            # Return the piece at the position
            return self.board[row][col]
        else:
            # Return None if the position is outside the board
            return None

    # Define a method to set the piece at a given position
    def set_piece(self, row, col, piece):
        # Check if the position is within the board
        if row >= 0 and row < GRID_SIZE and col >= 0 and col < GRID_SIZE:
            # Set the piece at the position
            self.board[row][col] = piece

    # Define a method to move a piece from one position to another
    def move_piece(self, from_row, from_col, to_row, to_col):
        global turn

        # Get the piece at the from position
        piece = self.get_piece(from_row, from_col)

        # Check if the piece exists and it is the right turn
        if piece is not None and ((turn and piece.color == WHITE) or (not turn and piece.color == BLACK)):
            # Get the possible moves for the piece
            moves = piece.get_possible_moves(from_row, from_col, self)

            # Check if the to position is in the possible moves
            if (to_row, to_col) in moves:
                # Move the piece to the to position and clear the from position
                self.set_piece(to_row, to_col, piece)
                self.set_piece(from_row, from_col, None)

                # Switch the turn
                turn = not turn

                sfx.play()
        # Define a method to draw the selected piece and its possible moves on the window
    def draw_selected(self, row, col):
    # Get the piece at the position
        piece = self.get_piece(row, col)

        # Check if the piece exists
        if piece is not None:
            # Calculate the position and size of the cell
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            w = CELL_SIZE
            h = CELL_SIZE

            # Draw a green border around the cell
            pygame.draw.rect(window, (0, 255, 0), (x, y, w, h), 5)

            # Draw the possible moves with yellow circles
            moves = piece.get_possible_moves(row, col, self)
            for move in moves:
                row = move[0]
                col = move[1]
                x = col * CELL_SIZE + CELL_SIZE // 2
                y = row * CELL_SIZE + CELL_SIZE // 2
                r = CELL_SIZE // 4
                pygame.draw.rect(window, (127, 127, 127), (x-r/2,y-r/2, r, r))

    # Define a method to check if a king is captured and end the game
    def check_game_over(self):
        global game_over
        numKings = 0

        # Loop through each row and column of the board
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                # Get the piece at the position
                piece = self.get_piece(row, col)

                # Check if it is a king
                if isinstance(piece, King):
                    # If a king is found in this row, note it down
                    numKings += 1
                    

        # If both kings aren't found, end the game
        if numKings <2:
            game_over = True
    def reset(self):
        # Loop through each row and column and fill the board with None values
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                self.board[row][col] = None

        # Create the pieces and place them on the board
        self.create_pieces()
    



# Define a class for the pieces
class Piece:
    # Define the constructor
    def __init__(self, color):
        # Set the color of the piece
        self.color = color

        # Load the image of the piece based on the color and the type
        self.image = pygame.image.load("sources/" + color_dict[self.color] + "_" + self.type + ".png")
        self.image = pygame.transform.scale (self.image, (128, 128))

    # Define a method to draw the piece on the window
    def draw(self, x, y):
        # Get the size of the image
        image_width = self.image.get_width()
        image_height = self.image.get_height()

        # Calculate the offset to center the image within the cell
        offset_x = (CELL_SIZE - image_width) // 2
        offset_y = (CELL_SIZE - image_height) // 2

        # Draw the image on the window
        window.blit(self.image, (x + offset_x, y + offset_y))

# Define a subclass for the knight
class Knight(Piece):
    # Define the type of the piece
    type = "knight"

    # Define a method to get the possible moves for the knight at a given position on a given board
    def get_possible_moves(self, row, col, board):
        # Define the offsets for the knight's moves
        offsets = [(-2,-1), (-2,+1), (-1,-2), (-1,+2), (+1,-2), (+1,+2), (+2,-1), (+2,+1)]

        # Loop through each offset and check if it is a valid move
        moves = []
        for offset in offsets:
            new_row = row + offset[0]
            new_col = col + offset[1]

            # Check if the new position is within the board
            if new_row >= 0 and new_row < GRID_SIZE and new_col >= 0 and new_col < GRID_SIZE:
                # Check if the new position is empty or has an enemy piece
                new_piece = board.get_piece(new_row, new_col)
                if new_piece is None or new_piece.color != self.color:
                    # Add the move to the list
                    moves.append((new_row, new_col))

        # Return the list of moves
        return moves

# Define a subclass for the rook
class Rook(Piece):
    # Define the type of the piece
    type = "rook"

    # Define a method to get the possible moves for the rook at a given position on a given board
    def get_possible_moves(self, row, col, board):
        # Define the directions for the rook's moves
        directions = [(-1,0), (+1,0), (0,-1), (0,+1)]

        # Loop through each direction and check if it is a valid move
        moves = []
        for direction in directions:
            # Start from the current position and move along the direction until hitting the edge or another piece
            new_row = row
            new_col = col
            while True:
                new_row += direction[0]
                new_col += direction[1]

                # Check if the new position is within the board
                if new_row >= 0 and new_row < GRID_SIZE and new_col >= 0 and new_col < GRID_SIZE:
                    # Check if the new position is empty or has an enemy piece
                    new_piece = board.get_piece(new_row, new_col)
                    if new_piece is None or new_piece.color != self.color:
                        # Add the move to the list
                        moves.append((new_row, new_col))

                        # If the new position has an enemy piece, stop moving along this direction
                        if new_piece is not None:
                            break
                    else:
                        # If the new position has a friendly piece, stop moving along this direction
                        break
                else:
                    # If the new position is outside the board, stop moving along this direction
                    break

        # Return the list of moves
        return moves

# Define a subclass for the bishop
class Bishop(Piece):
    # Define the type of the piece
    type = "bishop"

    # Define a method to get the possible moves for the bishop at a given position on a given board
    def get_possible_moves(self, row, col, board):
        # Define the directions for the bishop's moves
        directions = [(-1,-1), (-1,+1), (+1,-1), (+1,+1)]

        # Loop through each direction and check if it is a valid move
        moves = []
        for direction in directions:
            # Start from the current position and move along the direction until hitting the edge or another piece
            new_row = row
            new_col = col
            while True:
                new_row += direction[0]
                new_col += direction[1]

                # Check if the new position is within the board
                if new_row >= 0 and new_row < GRID_SIZE and new_col >= 0 and new_col < GRID_SIZE:
                    # Check if the new position is empty or has an enemy piece
                    new_piece = board.get_piece(new_row, new_col)
                    if new_piece is None or new_piece.color != self.color:
                        # Add the move to the list
                        moves.append((new_row, new_col))

                        # If the new position has an enemy piece, stop moving along this direction
                        if new_piece is not None:
                            break
                    else:
                        # If the new position has a friendly piece, stop moving along this direction
                        break
                else:
                    # If the new position is outside the board, stop moving along this direction
                    break

        # Return the list of moves
        return moves

# Define a subclass for the king
class King(Piece):
    # Define the type of the piece
    type = "king"

    # Define a method to get the possible moves for the king at a given position on a given board
    def get_possible_moves(self, row, col, board):
        # Define the offsets for the king's moves
        offsets = [(-1,-1), (-1,+1), (+1,-1), (+1,+1), (-1,0), (+1,0), (0,-1), (0,+1)]

        # Loop through each offset and check if it is a valid move
        moves = []
        for offset in offsets:
            new_row = row + offset[0]
            new_col = col + offset[1]

            # Check if the new position is within the board
            if new_row >= 0 and new_row < GRID_SIZE and new_col >= 0 and new_col < GRID_SIZE:
                # Check if the new position is empty or has an enemy piece
                new_piece = board.get_piece(new_row, new_col)
                if new_piece is None or new_piece.color != self.color:
                    # Add the move to the list
                    moves.append((new_row, new_col))

        # Return the list of moves
        return moves

# Define a subclass for the queen
class Queen(Piece):
    # Define the type of the piece
    type = "queen"

    # Define a method to get the possible moves for the queen at a given position on a given board
    def get_possible_moves(self, row, col, board):
        # Define the directions for the queen's moves
        directions = [(-1,-1), (-1,+1), (+1,-1), (+1,+1), (-1,0), (+1,0), (0,-1), (0,+1)]

        # Loop through each direction and check if it is a valid move
        moves = []
        for direction in directions:
            # Start from the current position and move along the direction until hitting the edge or another piece
            new_row = row
            new_col = col
            while True:
                new_row += direction[0]
                new_col += direction[1]

                # Check if the new position is within the board
                if new_row >= 0 and new_row < GRID_SIZE and new_col >= 0 and new_col < GRID_SIZE:
                    # Check if the new position is empty or has an enemy piece
                    new_piece = board.get_piece(new_row, new_col)
                    if new_piece is None or new_piece.color != self.color:
                        # Add the move to the list
                        moves.append((new_row, new_col))

                        # If the new position has an enemy piece, stop moving along this direction
                        if new_piece is not None:
                            break
                    else:
                        # If the new position has a friendly piece, stop moving along this direction
                        break
                else:
                    # If the new position is outside the board, stop moving along this direction
                    break

        # Return the list of moves
        return moves

# Create a board object
board = Board()

# Create a statistics object
statistics = Statistics()

title_screen = TitleScreen()
title_screen_active = True

# Define selected piece and its position
selected_piece = None
selected_row = -1
selected_col = -1

pygame.mixer.music.play(-1)

# Define a variable to store the current color scheme index
color_scheme_index = 0


# Define the main loop
running = True
async def main():
    global title_screen_active
    global game_over 
    global turn
    global board
    global statistics
    global color_scheme_index
    global running
    global selected_piece
    global color_schemes
    global challenge_illegal
    global selected_row
    global selected_column
    global computer_color


    
    while running:
        
        if title_screen_active:
            title_screen.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    title_screen_active = False
                    statistics.reset()
        else:
            # Handle events
            for event in pygame.event.get():
                # Check if the user wants to quit
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # Check if the user presses the spacebar
                    if event.key == pygame.K_SPACE:
                        # Increment the color scheme index and wrap around if necessary
                        color_scheme_index += 1
                        if color_scheme_index >= len(color_schemes):
                            color_scheme_index = 0
                # Check if the user clicks the mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    challenge_illegal = False

                    # Get the mouse position
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Get clicked row/col
                    row = mouse_y // CELL_SIZE    
                    col = mouse_x // CELL_SIZE

                    # Get the clicked piece
                    clicked_piece = board.get_piece(row, col)
                    
                    # If a piece is already selected
                    if selected_piece:
                        

                        # If clicked piece is same color as selected
                        if clicked_piece and clicked_piece.color == selected_piece.color:
                            # Select the new piece
                            selected_piece = clicked_piece
                            selected_row = row
                            selected_col = col

                        # If clicked on a valid move position
                        elif (row, col) in selected_piece.get_possible_moves(selected_row, selected_col, board):
                            # implement no capture for 5 moves
                            if (clicked_piece != None):
                                if clicked_piece.color != selected_piece.color and statistics.challenge_moves <5 and statistics.challenge == "No captures for 5 moves":
                                    challenge_illegal = True
                            #implement 1 square max 
                            if  (abs(row - selected_row) > 1 or abs(col - selected_col) > 1) and statistics.challenge == "Pieces can move at most 1 square" :
                                challenge_illegal = True  
                            #implement knights/bishop only
                            if ((selected_piece.type != "knight") and (selected_piece.type !="bishop")) and statistics.challenge == "Only knights and bishops can move":
                                challenge_illegal = True  
                            
                            # Move the piece if not challenge illegal

                            if  not challenge_illegal:
                                board.move_piece(selected_row, selected_col, row, col)
                                statistics.challenge_moves += 1

                            # Clear selection
                            selected_piece = None
                            selected_row = -1
                            selected_col = -1
                    
                        # Keep existing selection
                        else:
                            selected_piece = None
                            selected_row = -1
                            selected_column = -1

                    # If no piece selected yet    
                    else:
                        # Select the piece if right turn
                        if (clicked_piece != None):
                            
                            if (turn and clicked_piece.color == WHITE) or ((not turn) and clicked_piece.color == BLACK):
                                selected_piece = clicked_piece
                                selected_row = row
                                selected_col = col
                                
                        else:
                            pass

                    
                

            # Check for game over after handling the click
            board.check_game_over()
                        

            # Clear the window
            window.fill(BLACK)

            # Draw the board on the window
            board.draw(color_schemes[color_scheme_index])

            # Draw the selected piece and its possible moves on the window
            if selected_piece is not None:
                board.draw_selected(selected_row, selected_col)

            #Update the statistics
            statistics.update()
            #Draw the statistics
            statistics.draw()
            
            # Draw the game over message on the window if the game is over
            if game_over:
                draw_game_over()
                board.draw(color_schemes[color_scheme_index])
                statistics.num_challenges_completed += 1
                if statistics.num_challenges_completed == 5:
                    title_screen_active = True
                statistics.handle_new_round()
                board.reset()
                game_over = False
                turn = True
            
            if not game_over:
                if not turn and computer_color == BLACK:
                    possible_moves = []
                    for row in range(GRID_SIZE):
                        for col in range(GRID_SIZE):
                            piece = board.get_piece(row, col)
                            if piece is not None and piece.color == computer_color:
                                moves = piece.get_possible_moves(row, col, board)
                                for move in moves:
                                    computer_selected_piece = piece
                                    computer_clicked_piece = board.get_piece(move[0], move[1])
                                    
                                    computer_challenge_illegal = False
                                    computer_selected_row = move[0]
                                    computer_selected_col = move[1]
                                    
                                    if (computer_clicked_piece != None):
                                    #implement 5 move rule
                                        if computer_clicked_piece.color != computer_selected_piece.color and statistics.challenge_moves <5 and statistics.challenge == "No captures for 5 moves":
                                            computer_challenge_illegal = True
                                    #implement 1 square max 
                                    if  (abs(row - computer_selected_row) > 1 or abs(col - computer_selected_col )>1) and statistics.challenge == "Pieces can move at most 1 square" :
                                        computer_challenge_illegal = True  
                                    #implement knights/bishop only
                                    if ((computer_selected_piece.type != "knight") and (computer_selected_piece.type !="bishop")) and statistics.challenge == "Only knights and bishops can move":
                                        computer_challenge_illegal = True
                                    
                                    if not computer_challenge_illegal:
                                        possible_moves.append((row, col, move[0], move[1]))
                    
                    if possible_moves:
                        random_move = random.choice(possible_moves)
                        board.move_piece(random_move[0], random_move[1], random_move[2], random_move[3])

                

        # Update the display
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        clock.tick(60)

        await asyncio.sleep(0)

# Quit pygame
#pygame.quit()

asyncio.run(main())