from agents_and_games.utils.players import Players


class TicTacToe:
    def __init__(self):
        self.n = 3
        self.board = None
        self.player = None

        self.init_board()
        self.init_player()

    def init_board(self):
        self.board = [[Players.EMPTY.value for _ in range(self.n)] for _ in range(self.n)]

    def init_player(self, player: str = Players.P1.value):
        self.player = player

    def switch_player(self):
        self.player = Players.P2.value if self.player == Players.P1.value else Players.P1.value

    def make_move(self, move: tuple[int, int]) -> None:
        self.board[move[0]][move[1]] = self.player
        self.switch_player()

    def undo_move(self, move: tuple[int, int]) -> None:
        self.board[move[0]][move[1]] = Players.EMPTY.value
        self.switch_player()

    def is_valid_move(self, move: tuple[int, int]) -> bool:
        return 0 <= move[0] < self.n and \
               0 <= move[1] < self.n and \
               self.board[move[0]][move[1]] == Players.EMPTY.value

    def is_winner(self, player: str, board = None) -> bool:
        if board is None:
            board = self.board
        for i in range(self.n):
            if all(board[i][j] == player for j in range(self.n)) or \
               all(board[j][i] == player for j in range(self.n)):
                return True
        return all(board[i][i] == player for i in range(self.n)) or \
               all(board[i][self.n - 1 - i] == player for i in range(self.n))

    def is_draw(self, board = None) -> bool:
        if board is None:
            board = self.board
        return not any(cell == Players.EMPTY.value for row in board for cell in row)

    def is_game_over(self) -> bool:
        return self.is_winner(player=Players.P1.value) or \
               self.is_winner(player=Players.P2.value) or \
               self.is_draw()

    def get_valid_moves(self) -> list[tuple[int, int]]:
        return [(i, j) for i in range(self.n) for j in range(self.n) if self.board[i][j] == Players.EMPTY.value]

    def display_board(self):
        line_horizontal = " ---" * self.n + " "
        print(line_horizontal)
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            print(line_horizontal)

    def play_game(self, player_1, player_2):
        turn = 0
        while not self.is_game_over():
            turn += 1
            self.display_board()
            print()
            print(f"== Turn {turn:02} ==")
            if turn % 2:
                move = player_1.get_move(game=self)
            else:
                move = player_2.get_move(game=self)
            self.make_move(move=move)

        self.display_board()
        if self.is_winner(player=Players.P1.value):
            print(f"{Players.P1.value} wins!")
        elif self.is_winner(player=Players.P2.value):
            print(f"{Players.P2.value} wins!")
        else:
            print("It's a draw!")
