import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pygame
from pygame import mixer
import os



class Connect4:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect 4")

        self.canvas = tk.Canvas(root, width=700, height=600, bg='black')
        self.canvas.pack()

        self.draw_board()
        
        self.player = 1
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        self.canvas.bind("<Button-1>", self.drop_piece)

    def draw_board(self):
        for i in range(6):
            for j in range(7):
                x1 = 100 + j * 80
                y1 = 100 + i * 80
                x2 = x1 + 70
                y2 = y1 + 70
                self.canvas.create_oval(x1, y1, x2, y2, fill='white')

    def drop_piece(self, event):
        drop_sound.play()
        x = event.x
        col = (x - 100) // 80
        row = -1
        for i in range(5, -1, -1):
            if self.board[i][col] == 0:
                row = i
                break
        if row == -1:
            return
        color = 'red' if self.player == 1 else 'yellow'
        x1 = 100 + col * 80
        y1 = 100 + row * 80
        x2 = x1 + 70
        y2 = y1 + 70
        self.canvas.create_oval(x1, y1, x2, y2, fill=color)
        self.board[row][col] = self.player
        if self.check_win():
            winner = "Player 1" if self.player == 1 else "Player 2"
            self.canvas.create_text(350, 50, text=f"{winner} wins!", font=("Arial", 36), fill="white")
            self.canvas.unbind("<Button-1>")
            drop_sound.stop()
            win_sound.play()
            self.game_over(winner)

        else:
            num_filled = sum(1 for row in self.board for cell in row if cell != 0)
            if num_filled == 42:
                self.canvas.create_text(350, 50, text="Tie game!", font=("Arial", 36), fill="white")
                self.canvas.unbind("<Button-1>")
                drop_sound.stop()
                self.game_over(None)
            else:
                self.player = 3 - self.player



    def check_win(self):
        for i in range(6):
            for j in range(4):
                if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] != 0:
                    return True
        for i in range(3):
            for j in range(7):
                if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] != 0:
                    return True
        for i in range(3):
            for j in range(4):
                if self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3] != 0:
                    return True
        for i in range(3, 6):
            for j in range(4):
                if self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2] == self.board[i-3][j+3] != 0:
                    return True
        return False
    

    def game_over(self, winner):
        message = f"{winner} wins!\n\nDo you want to start a new game or go back to the main menu?"
        choice = messagebox.askquestion("Game Over", message)
        if choice == "yes":
            # Start a new game
            self.canvas.destroy()  # Destroy the current game window
            game_window = tk.Tk()
            game_window.title("Connect 4")
            game_window.geometry('1000x600')
            game = Connect4(game_window)
            game_window.mainloop()
        else:
            # Go back to the main menu
            self.canvas.destroy()  # Destroy the current game window
            #connect4_game()


# initialize pygame mixer
pygame.mixer.init()

# get the current working directory
cwd = os.getcwd()

# create the full path to the sound file using os.path.join()
file_path_1 = os.path.join(cwd, "C:/Users/Rishi/Downloads/ball_sound.mpeg")
file_path_2 = os.path.join(cwd, "C:/Users/Rishi/Downloads/winsound.mpeg")
# load the sound effect file
drop_sound = pygame.mixer.Sound(file_path_1)
win_sound = pygame.mixer.Sound(file_path_2)
def drop_piece(grid, row, col, piece):
    grid[row][col] = piece
    drop_sound.play()

def check_win(self):
    win_sound.play()


def connect4_game():
    top.destroy()
    game_window = tk.Tk()
    game_window.title("Connect 4")
    game_window.geometry('800x600')
    game = Connect4(game_window)
    game_window.mainloop()
    drop_sound.stop()

def show_help():
    #messagebox.showinfo("Help", "This will display game rules")
    if messagebox.askyesno("Help", "Hi! am your assistance button.\nDo you want to know the rules of the game?"):
        show_rules()

def show_rules():
    rules_window = tk.Toplevel()
    #messagebox.showinfo("Help", "This is help message")
    rules_window.title("Game Rules")
    rules_window.geometry('1500x600')
    rules_text = """
    Connect 4 game description :

    The game is played on a vertical board that has seven hollow columns and six rows. 
    Each column has a hole in the upper part of the board, where pieces are introduced. 
    There is a window in the lower part of the board to see the pieces that are introduced from the top. 
    The objective of the game is to connect four of one's own pieces of the same color next to each other vertically, horizontally, or diagonally before your opponent does.

    Rules:
    1. The game starts with an empty board.
    2. Players take turns placing their colored pieces into the board.
    3. Pieces must be dropped into an open column, and will fall to the lowest open slot in that column.
    4. The first player to get four of their pieces in a row wins the game.
    5. If the board is full and no player has four in a row, the game is a tie.

    """
    rules_label = tk.Label(rules_window, text=rules_text, font=("Arial", 12), justify='left')
    rules_label.pack(padx=20, pady=20)

def quit_game():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        top.destroy()



# Create the main window
top = tk.Tk()
top.title("Connect4")
top.geometry('1500x680')

# Load the background image
bg = tk.PhotoImage(file="C:/Users/Rishi/OneDrive/Desktop/bg.png")
label1 = tk.Label(top, image=bg)
label1.place(x=0, y=0)

# Load the button images
start_img = tk.PhotoImage(file=r"C:/Users/Rishi/OneDrive/Desktop/start.png")
help_img = tk.PhotoImage(file="C:/Users/Rishi/OneDrive/Desktop/help.png")
quit_img = tk.PhotoImage(file="C:/Users/Rishi/OneDrive/Desktop/quit.png")


# Create the buttons with images
b1 = tk.Button(top, image=start_img, borderwidth=0, height = 70, width = 320, highlightthickness=0, command=connect4_game)
b1.place(x=25, y=100)

b2 = tk.Button(top, image=help_img, borderwidth=0, height = 70, width = 320, highlightthickness=0, command=show_help)
b2.place(x=25, y=300)

b3 = tk.Button(top, image=quit_img, borderwidth=0,height = 70, width = 320, highlightthickness=0, command=quit_game)
b3.place(x=25, y=500)


top.mainloop()


