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
    self.squares = squares
    self.board = self.calculate_squares(squares)

  def calculate_squares(self, squares):
    dic_board = {}
    for i in range(squares):
      dic_board[str(i+1)] = ' '
    return dic_board
  
  def display_board(self):
    display_board = "\n"
    for square in self.board.keys():
      if int(square) % 3 != 0:
        display_board += f"{self.board[square]}|"
      else:
        display_board += f"{self.board[square]}"

      if int(square) % 3 == 0 and int(square) != 9:
        display_board += f"\n{"-" * 5}\n"

    display_board += "\n"

    return display_board
  
  def add_symbol_to_board(self, symbol, position):
    if position not in self.board or symbol == None:
      raise AttributeError
    
    if self.board[position] in ['X', 'O']:
      return -1
    
    self.board[position] = symbol
    return 0
  
  def player_turn(self, player: Player, turn: int):
    print(f"Turn Nº: {turn}")
    position = -999
    while position not in self.board:
      position = input(f"{player.name} select the square base on range 1-9 position. Position: ")
    
    try:
      result = self.add_symbol_to_board(player.symbol, position)
      while result == -1:
        print(f"{player.name} the square you select it's already occupied, please try again")
        position = -999
        while position not in self.board:
          position = input(f"{player.name} select the square base on range 1-9 position. Position: ")

        result = self.add_symbol_to_board(player.symbol, position)

      is_game_finish = self.is_finish(player)
      
      if is_game_finish:
        print(f"\n{player.name} won Tic Tac Toe Match!! Congrats!!\n")
        return is_game_finish

    except Exception as e:
      print(f"Error, try again. Error: {e}")

    print(self.display_board())
    return self.all_squares_occupaid()

  def all_squares_occupaid(self):
    square_desoccupaid = 0
    for square in self.board.values():
      if square == " ":
        square_desoccupaid += 1

    if square_desoccupaid == 0:
      print("\nIt's a tie...\n")
      return True
    
    return False

  def is_finish(self, player):

      posible_results = {
        0: [1, 2, 3],
        1: [4, 5, 6],
        2: [7, 8, 9],
        3: [1, 4, 7],
        4: [2, 5, 8],
        5: [3, 6, 9],
        6: [1, 5, 9],
        7: [3, 5, 7]
      }

      player_moves = {
        int(square)
        for square, symbol in self.board.items()
        if symbol == player.symbol
      }

      for win_combo in posible_results.values():
        if set(win_combo).issubset(player_moves):
          return True
        
      return False

      
