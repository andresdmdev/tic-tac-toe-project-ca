from models import Player, Board

print("Welcome to Tic Tac Toe Game!")
print("Let's begin with presentations of the players.")
player1 = Player(input("Player 1, please enter your name: "))
player1.choose_symbol()
player2 = Player(input("Player 2, please enter your name: "))
player2.choose_symbol(player1.symbol)

print(f"Welcome {player1.name}({player1.symbol}) and {player2.name}({player2.symbol})! Let's start the game!")

print("Here is the board:")

board = Board()
print(board.display_board())