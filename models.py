class Player:
  def __init__(self, name):
    self.name = name
    self.symbol = None
  
  def choose_symbol(self, symbol = None):

    if symbol:
      if symbol == 'X':
        self.symbol = 'O'
      else:
        self.symbol = 'X'
      return

    self.symbol = input(f"{self.name}, please choose your symbol (X or O): ")
    while self.symbol not in ['X', 'O']:
      self.symbol = input(f"{self.name}, please choose your symbol (X or O): ")

class Board:
  def __init__(self, squares = 9):
    self.board = self.calculate_squares(squares)

  def calculate_squares(self, squares):
    dic_board = {}
    for i in range(squares):
      dic_board[str(i+1)] = ''
    return dic_board
  
  def display_board(self):
    display_board = "\n"
    for square in self.board.keys():
      if int(square) % 3 != 0:
        display_board += f" {self.board[square]}|"
      else:
        display_board += f"{self.board[square]}"

      if int(square) % 3 == 0 and int(square) != 9:
        display_board += f"\n{"-" * 5}\n"

    display_board += "\n"

    return display_board
