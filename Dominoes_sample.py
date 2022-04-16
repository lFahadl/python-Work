import random

# Write your code here
class Dominoes:
    def __init__(self):
        self.dominoes = []
        self.stock_pieces: list[list[int]] = []
        self.computer_pieces: list[list[int]] = []
        self.player_pieces: list[list[int]] = []
        self.domino_snake = [[-1, -1]]
        self.status = None
        self.num_map = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        for i in range(0, 7):
            for j in range(i, 7):
                self.dominoes.append([i, j])
        self.deal_pieces()

    def deal_pieces(self):
        while self.domino_snake == [[-1, -1]]:
            self.stock_pieces = self.dominoes.copy()
            self.computer_pieces = random.sample(self.stock_pieces, 7)
            self.stock_pieces = [piece for piece in self.stock_pieces if piece not in self.computer_pieces]
            self.player_pieces = random.sample(self.stock_pieces, 7)
            self.stock_pieces = [piece for piece in self.stock_pieces if piece not in self.player_pieces]
            current_max = [-1, -1]
            for i in range(7):
                if self.computer_pieces[i][0] == self.computer_pieces[i][1]:
                    if current_max[0] < self.computer_pieces[i][0]:
                        current_max = self.computer_pieces[i]
                        self.status = "computer"
                if self.player_pieces[i][0] == self.player_pieces[i][1]:
                    if current_max[0] < self.player_pieces[i][0]:
                        current_max = self.player_pieces[i]
                        self.status = "player"
            self.domino_snake = [current_max]
        if self.status == 'player':
            self.player_pieces.remove(self.domino_snake[0])
            self.status = "computer"
        else:
            self.computer_pieces.remove(self.domino_snake[0])
            self.status = "player"
        self.num_map[self.domino_snake[0][0]] += 1
        self.num_map[self.domino_snake[0][1]] += 1

    def printer(self):
        print("=" * 70)
        print("Stock size: ", len(self.stock_pieces))
        print("Computer pieces: ", len(self.computer_pieces))
        print()
        if len(self.domino_snake) <= 6:
            print(*self.domino_snake, sep = "")
        else:
            print(*self.domino_snake[0:3], sep = "", end = "...")
            print(*self.domino_snake[-3:], sep = "")
        print()
        print("Your pieces:")
        for i, piece in enumerate(self.player_pieces):
            print(f"{i + 1}:{piece}")
        print()

    def computer_won(self):
        return len(self.computer_pieces) == 0

    def player_won(self):
        return len(self.player_pieces) == 0

    def is_draw(self):
        return self.domino_snake[0][0] == self.domino_snake[-1][1] \
               and self.num_map[self.domino_snake[0][0]] == 8

    def computer_move(self):
        input("Status: Computer is about to make a move. Press Enter to continue...")
        limit = len(self.computer_pieces)
        option = random.randint(-limit, limit)
        self.make_move(option, self.computer_pieces)
        self.status = "player"

    def player_move(self):
        limit = len(self.computer_pieces)
        user_input = input("Status: It's your turn to make a move. Enter your command. ")
        while True:
            option = int(user_input) if user_input.removeprefix("-").isdecimal() else None
            if option is not None and -limit <= option <= limit:
                break
            else:
                user_input = input("Invalid input. Please try again.")
        self.make_move(option, self.player_pieces)
        self.status = "computer"

    def make_move(self, option, pieces):
        if option == 0:
            piece = random.choice(self.stock_pieces)
            pieces.append(piece)
            self.stock_pieces.remove(piece)
        elif option < 0:
            self.domino_snake.insert(0, pieces[-option - 1])
            del pieces[-option - 1]
        else:
            self.domino_snake.append(pieces[option - 1])
            del pieces[option - 1]

    def play(self):
        while not self.computer_won() \
                and not self.player_won() \
                and not self.is_draw():
            self.printer()
            if self.status == "computer":
                self.computer_move()
            else:
                self.player_move()

if __name__ == '__main__':
    game = Dominoes()
    game.play()
    game.printer()
    winner = None
    if game.player_won():
        winner = "You won!"
    elif game.computer_won():
        winner = "The computer won!"
    else:
        winner = "It's a draw!"
    print("Status: The game is over.", winner)
    