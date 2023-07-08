class TicTacToe:
    def __init__(self):
        self.player = 'x'
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

    def action(self, field):
        row, column = field
        self.board[row][column] = self.player

        if not self.check_win():
            self.player = 'x' if self.player == 'o' else 'o'

    def check_win(self):
        for row in self.board:
            if all(field == self.player for field in row):
                return True

        for row in self.transpose(self.board):
            if all(field == self.player for field in row):
                return True

        if all([self.board[0][0] == self.player, self.board[1][1] == self.player, self.board[2][2] == self.player]):
            return True

        if all([self.board[0][2] == self.player, self.board[1][1] == self.player, self.board[2][0] == self.player]):
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if any(field == ' ' for field in row):
                return False
        if self.check_draw():
            return False
        return True

    def transpose(self, matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
