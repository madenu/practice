class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dead_or_alive = {}
        for outtie in range(len(board)):
            for innie in range(len(board[0])):

                alive_neighbors = 0
                for outty in range(max(0, outtie - 1), min(outtie + 2, len(board))):
                    for inny in range(max(0, innie - 1), min(innie + 2, len(board[0]))):
                        if (outty, inny) == (outtie, innie):
                            continue
                        alive_neighbors = alive_neighbors + board[outty][inny]

                dead_or_alive[(outtie, innie)] = (board[outtie][innie], alive_neighbors)

        for outtie in range(len(board)):  # rows (up/down) (vert)
            for innie in range(len(board[0])):  # cols (left/right) (horiz)
                alive_neighbors = dead_or_alive[(outtie, innie)][1]
                if alive_neighbors == 3:  # birth
                    board[outtie][innie] = 1
                elif alive_neighbors < 2:  # loneliness
                    board[outtie][innie] = 0
                elif alive_neighbors > 3:  # overpopulation
                    board[outtie][innie] = 0


def _check_board(actual, expected):
    for ii in range(len(expected)):
        for jj in range(len(expected[0])):
            if actual[ii][jj] != expected[ii][jj]:
                return False
    return True


if __name__ == '__main__':
    sol = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    sol.gameOfLife(board)
    assert _check_board(board, expected)
