import tkinter as tk

class ChessboardApp:
    def __init__(self, root, rows, columns):
        self.root = root
        self.rows = rows
        self.columns = columns
        self.selected_piece = None
        self.board = None
        self.create_board()

    def handle_click(self, row, col):
        if self.selected_piece is None:
            self.select_piece(row, col)
        else:
            self.move_piece(row, col)

    def select_piece(self, row, col):
        if self.board[row][col] != "":
            self.selected_piece = (row, col)
            self.highlight_moves(row, col)

    def move_piece(self, row, col):
        if (row, col) in self.available_moves:
            self.board[self.selected_piece[0]][self.selected_piece[1]] = ""
            self.board[row][col] = self.board[self.selected_piece[0]][self.selected_piece[1]]
            self.selected_piece = None
            self.clear_highlights()
            self.redraw_board()

    def highlight_moves(self, row, col):
        self.available_moves = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
        for move in self.available_moves:
            if 0 <= move[0] < self.rows and 0 <= move[1] < self.columns:
                self.labels[move[0]][move[1]].configure(bg="yellow")

    def clear_highlights(self):
        for row in range(self.rows):
            for col in range(self.columns):
                self.labels[row][col].configure(bg="white" if (row + col) % 2 == 0 else "light gray")

    def create_board(self):
        self.board = [["" for _ in range(self.columns)] for _ in range(self.rows)]
        self.labels = []

        for row in range(self.rows):
            current_row = []
            for col in range(self.columns):
                square_color = "white" if (row + col) % 2 == 0 else "light gray"
                label = tk.Label(self.root, bg=square_color, width=4, height=2, font=("Arial", 24), borderwidth=1, relief="solid")
                label.grid(row=row, column=col, sticky="nsew")
                label.bind("<Button-1>", lambda event, row=row, col=col: self.handle_click(row, col))
                current_row.append(label)
            self.labels.append(current_row)

        # Inicjalizacja pionków na planszy
        self.board[1][1] = "♙"
        self.labels[1][1].configure(text="♙")
        self.board[6][6] = "♟"
        self.labels[6][6].configure(text="♟")

    def redraw_board(self):
        for row in range(self.rows):
            for col in range(self.columns):
                self.labels[row][col].destroy()
        self.create_board()

root = tk.Tk()
root.title("Szachownica")

app = ChessboardApp(root, 8, 8)

root.mainloop()

'''
import tkinter as tk

def handle_click(row, col):
    print(f"Kliknięto pole [{row}, {col}]")

def create_board(root, rows, columns):
    board = tk.Frame(root)
    board.pack(fill=tk.BOTH, expand=True)

    for row in range(rows):
        for col in range(columns):
            square_color = "white" if (row + col) % 2 == 0 else "light gray"
            square = tk.Frame(board, bg=square_color, width=50, height=50)
            square.grid(row=row, column=col, sticky="nsew")
            square.bind("<Button-1>", lambda event, row=row, col=col: handle_click(row, col))
            board.grid_rowconfigure(row, weight=1)
            board.grid_columnconfigure(col, weight=1)

            # Dodajemy figury na planszę
            if row == 1:
                label = tk.Label(square, text="♙", font=("Arial", 24), bg=square_color)
                label.pack(expand=True)
                label.bind("<Button-1>", lambda event, row=row, col=col: handle_click(row, col))
                label.configure(bg=square_color)  # Ustawiamy przezroczyste tło dla pionka
            elif row == 6:
                label = tk.Label(square, text="♟", font=("Arial", 24), bg=square_color)
                label.pack(expand=True)
                label.bind("<Button-1>", lambda event, row=row, col=col: handle_click(row, col))
                label.configure(bg=square_color)  # Ustawiamy przezroczyste tło dla pionka
            elif row == 0 or row == 7:
                if col == 0 or col == 7:
                    label = tk.Label(square, text="♖", font=("Arial", 24), bg=square_color)
                    label.pack(expand=True)
                    label.bind("<Button-1>", lambda event, row=row, col=col: handle_click(row, col))
                    label.configure(bg=square_color)  # Ustawiamy przezroczyste tło dla pionka
                elif col == 1 or col == 6:
                    label = tk.Label(square, text="♘", font=("Arial", 24), bg=square_color)
                    label.pack(expand=True)
                    label.bind("<Button-1>", lambda event, row=row, col=col: handle_click(row, col))
                    label.configure(bg=square_color)  # Ustawiamy przezroczyste tło dla pionka
                elif col == 2 or col == 5:
                    label = tk.Label(square, text="♗", font=("Arial", 24), bg=square_color)
                    label.pack(expand=True)
                    label.bind("<Button-1>", lambda event, row=row, col=col: handle_click(row, col))
                    label.configure(bg=square_color)  # Ustawiamy przezroczyste tło dla pionka
                elif col == 3:
                    label = tk.Label(square, text="♕", font=("Arial", 24), bg=square_color)
                    label.pack(expand=True)
                    label.bind("<Button-1>", lambda event, row=row, col=col: handle_click(row, col))
                    label.configure(bg=square_color)  # Ustawiamy przezroczyste tło dla pionka
                elif col == 4:
                    label = tk.Label(square, text="♔", font=("Arial", 24), bg=square_color)
                    label.pack(expand=True)
                    label.bind("<Button-1>", lambda event, row=row, col=col: handle_click(row, col))
                    label.configure(bg=square_color)  # Ustawiamy przezroczyste tło dla pionka

root = tk.Tk()
root.title("Szachownica")


create_board(root,8,8)

root.mainloop()'''
