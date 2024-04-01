import numpy as np


class Env:
    def __init__(self, preenv=None):
        if type(preenv) != type(None):
            self.board = preenv.board.copy()
            self.nextplayer = preenv.nextplayer
        else:
            self.board = np.zeros((3, 3))
            self.nextplayer = None

    def put(self, x, y, symbol="x"):
        if self.nextplayer:
            assert self.nextplayer == symbol

        val = -1 if symbol == "x" else 1

        if self.board[x, y] == 0:
            self.board[x, y] = val
            self.nextplayer = "o" if symbol == "x" else "x"
            return True
        else:
            return False

    def get(self):
        moves = list(zip(*np.where(self.board == 0)))
        boards = []
        for x, y in moves:
            _env = Env(self)
            _env.put(x, y, symbol=self.nextplayer)
            boards.append(_env)
        return boards,moves

    def gameover(self):
        winner = 0
        boardfull = False
        
        m, n = self.board.shape
        assert m == n
        boardplus, boardminus = self.board.copy() + 1, self.board.copy() - 1

        for i in range(m):
            if np.any(boardplus[i, :]) == False:
                winner = -1

            if np.any(boardminus[i, :]) == False:
                winner = 1

        for j in range(n):
            if np.any(boardplus[:, j]) == False:
                winner = -1
            if np.any(boardminus[:, j]) == False:
                winner = 1

        if np.any(boardplus.diagonal()) == False:
            winner = -1
        if np.any(boardminus.diagonal()) == False:
            winner = 1

        if np.any(np.fliplr(boardplus).diagonal()) == False:
            winner = -1
        if np.any(np.fliplr(boardminus).diagonal()) == False:
            winner = 1

        winner = ["x", "", "o"][winner + 1]
        howempty = (self.board == 0).sum()  # 100 - how empty the board is

        if winner != "":
            score = 100 - howempty 
        else:
            score = 0

        if howempty==0: # i.e, if board is full
            boardfull = True

        return winner, score, full

    def __str__(self):
        m, n = self.board.shape
        expr = "\n"
        for i in range(m):
            for j in range(n):
                val = self.board[i, j]
                if val == 0:
                    sym = "."
                elif val == 1:
                    sym = "o"
                else:
                    sym = "x"
                expr += sym + (" | " if not j == n - 1 else " ")

            expr += "\n.........\n" if not i == m - 1 else "\n"

        return expr.upper()


if __name__ == "__main__":
    env = Env()
    assert env.put(2, 1, "x")
    assert env.put(1, 1, "o")
    print(env)

    print(env.get())
