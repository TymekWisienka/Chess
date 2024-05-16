import tkinter as tk

class ChessboardApp:
    def __init__(self, root, rows, columns):
        self.root = root
        self.rows = rows
        self.columns = columns
        self.selected_piece = None
        self.board = [["" for _ in range(self.columns)] for _ in range(self.rows)]
        self.labels = []
        self.color = 'white'
        self.create_board()
        self.initialize_pieces()

    def handle_click(self, row, col):
        if self.selected_piece is None:
            self.select_piece(row, col)
        else:
            self.move_piece(row, col)

    def select_piece(self, row, col):
        piece = self.board[row][col]
        if (piece.islower() and self.color == "white") or (piece.isupper() and self.color == "black"):
            self.selected_piece = (row, col)
            self.highlight_moves(row, col)

    def move_piece(self, row, col):
        if (row, col) in self.available_moves:
            piece = self.board[self.selected_piece[0]][self.selected_piece[1]]
            self.board[self.selected_piece[0]][self.selected_piece[1]] = ""
            self.board[row][col] = piece
            self.selected_piece = None
            self.clear_highlights()
            self.update_labels()
            self.color = 'black' if self.color == 'white' else 'white'

    def highlight_moves(self, row, col):
        self.available_moves = []
        piece = self.board[row][col]
        # Simplified movement rules
        if piece.lower() == "p":  # Pawn
            direction = 1 if piece.islower() else -1
            if 0 <= row + direction < self.rows:
                self.available_moves.append((row + direction, col))
        elif piece.lower() == "r":  # Rook
            for i in range(self.rows):
                if i != row:
                    self.available_moves.append((i, col))
            for j in range(self.columns):
                if j != col:
                    self.available_moves.append((row, j))
        elif piece.lower() == "n":  # Knight
            moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
            for dx, dy in moves:
                if 0 <= row + dx < self.rows and 0 <= col + dy < self.columns:
                    self.available_moves.append((row + dx, col + dy))
        elif piece.lower() == "b":  # Bishop
            for i in range(1, self.rows):
                if 0 <= row + i < self.rows and 0 <= col + i < self.columns:
                    self.available_moves.append((row + i, col + i))
                if 0 <= row - i < self.rows and 0 <= col - i < self.columns:
                    self.available_moves.append((row - i, col - i))
                if 0 <= row + i < self.rows and 0 <= col - i < self.columns:
                    self.available_moves.append((row + i, col - i))
                if 0 <= row - i < self.rows and 0 <= col + i < self.columns:
                    self.available_moves.append((row - i, col + i))
        elif piece.lower() == "q":  # Queen
            for i in range(self.rows):
                if i != row:
                    self.available_moves.append((i, col))
            for j in range(self.columns):
                if j != col:
                    self.available_moves.append((row, j))
            for i in range(1, self.rows):
                if 0 <= row + i < self.rows and 0 <= col + i < self.columns:
                    self.available_moves.append((row + i, col + i))
                if 0 <= row - i < self.rows and 0 <= col - i < self.columns:
                    self.available_moves.append((row - i, col - i))
                if 0 <= row + i < self.rows and 0 <= col - i < self.columns:
                    self.available_moves.append((row + i, col - i))
                if 0 <= row - i < self.rows and 0 <= col + i < self.columns:
                    self.available_moves.append((row - i, col + i))
        elif piece.lower() == "k":  # King
            moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dx, dy in moves:
                if 0 <= row + dx < self.rows and 0 <= col + dy < self.columns:
                    self.available_moves.append((row + dx, col + dy))

        for move in self.available_moves:
            if 0 <= move[0] < self.rows and 0 <= move[1] < self.columns:
                self.labels[move[0]][move[1]].configure(bg="yellow")

    def clear_highlights(self):
        for row in range(self.rows):
            for col in range(self.columns):
                self.labels[row][col].configure(bg="white" if (row + col) % 2 == 0 else "light gray")

    def create_board(self):
        for row in range(self.rows):
            current_row = []
            for col in range(self.columns):
                square_color = "white" if (row + col) % 2 == 0 else "light gray"
                label = tk.Label(self.root, bg=square_color, width=4, height=2, font=("Arial", 24), borderwidth=1, relief="solid")
                label.grid(row=row, column=col, sticky="nsew")
                label.bind("<Button-1>", lambda event, row=row, col=col: self.handle_click(row, col))
                current_row.append(label)
            self.labels.append(current_row)

    def initialize_pieces(self):
        # Inicjalizacja pionków
        for col in range(8):
            self.board[1][col] = "♙"
            self.board[6][col] = "♟"
        # Inicjalizacja wież
        self.board[0][0] = self.board[0][7] = "♖"
        self.board[7][0] = self.board[7][7] = "♜"
        # Inicjalizacja skoczków
        self.board[0][1] = self.board[0][6] = "♘"
        self.board[7][1] = self.board[7][6] = "♞"
        # Inicjalizacja gońców
        self.board[0][2] = self.board[0][5] = "♗"
        self.board[7][2] = self.board[7][5] = "♝"
        # Inicjalizacja królowej
        self.board[0][3] = "♕"
        self.board[7][3] = "♛"
        # Inicjalizacja króla
        self.board[0][4] = "♔"
        self.board[7][4] = "♚"

        self.update_labels()

    def update_labels(self):
        for row in range(self.rows):
            for col in range(self.columns):
                piece = self.board[row][col]
                self.labels[row][col].configure(text=piece)

root = tk.Tk()
root.title("Szachownica")

app = ChessboardApp(root, 8, 8)

root.mainloop()
