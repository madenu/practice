import random
from random import randint


class Square:
    k: int
    isHidden: bool
    isMine: bool
    neighbors: set

    def __init__(self, k, isHidden, isMine, neighbors):
        self.k = k
        self.isHidden = isHidden
        self.isMine = isMine
        self.neighbors = neighbors

    @staticmethod
    def to_coord(k, w, h) -> (int, int):
        ii = k % w
        jj = k // h
        return jj, ii

    @staticmethod
    def from_coord(jj, ii, h) -> int:
        return jj * h + ii

    def danger_lvl(self) -> int:
        return sum([1 for n in self.neighbors if n.isMine])


class GameState:
    board: list
    props: dict

    def __init__(self, board, props):
        self.board = board
        self.props = props


def make_board(width, height, num_mines):
    board = []

    # Initialize an empty board
    for jj in range(height):
        new_row = []
        for ii in range(width):
            new_row.append(Square(jj * width + ii, True, False, set()))
        board.append(new_row)

    # Connect neighbors
    for jj in range(height):
        for ii in range(width):
            target = board[jj][ii]
            top = jj - 1
            bottom = jj + 1
            right = ii + 1
            if bottom < height:  # Below
                neighbor = board[bottom][ii]
                neighbor.neighbors.add(target)
                target.neighbors.add(neighbor)
            if (bottom < height) and (right < width):  # Bottom Right
                neighbor = board[bottom][right]
                neighbor.neighbors.add(target)
                target.neighbors.add(neighbor)
            if right < width:  # Right
                neighbor = board[jj][right]
                neighbor.neighbors.add(target)
                target.neighbors.add(neighbor)
            if (top >= 0) and (right < width):  # Top Right
                neighbor = board[top][right]
                neighbor.neighbors.add(target)
                target.neighbors.add(neighbor)

    # Randomly place mines
    k_coords = [randint(0, height - 1) * width + randint(0, width - 1) for _ in range(num_mines)]

    while k_coords:
        k = k_coords.pop()
        xx = k % width
        yy = k // height
        target = board[yy][xx]
        if target.isMine:
            k_coords.append(randint(0, height - 1) * width + randint(0, width - 1))
        else:
            mine = Square(k, True, True, set())
            mine.neighbors.update(target.neighbors)
            for n in target.neighbors:
                n.neighbors.remove(target)
                n.neighbors.add(mine)
            board[yy][xx] = mine

    return board


# Mutates game state
def update(click_coord, game_state):
    jj, ii = click_coord
    board = game_state.board
    square = board[jj][ii]
    square.isHidden = False

    # Update board
    if square.danger_lvl() == 0:
        visited = set()
        stack = set([n for n in square.neighbors if not n.isMine])
        while stack:
            curr = stack.pop()
            if not (curr in visited):
                visited.add(curr)
                curr.isHidden = False
                if curr.danger_lvl() == 0:
                    stack.update([n for n in curr.neighbors if not n.isMine])

    # Check for end game
    num_uncovered_squares = sum([sum([1 for sq in row if not sq.isHidden]) for row in board])
    num_mines = sum([sum([1 for sq in row if sq.isMine]) for row in board])
    if square.isMine:
        game_state.props["isLoss"] = True
        return
    elif ((len(board[0]) * len(board)) - num_uncovered_squares) <= num_mines:
        game_state.props["isWin"] = True
        return


def render(game_state):
    output = ""
    board = game_state.board
    for jj in range(len(board)):
        output = output + "\n"
        for ii in range(len(board[0])):
            square = board[jj][ii]
            if square.isHidden:
                output = output + "- "
            elif square.isMine:
                output = output + "! "
            else:
                output = output + "%s " % square.danger_lvl()

    if game_state.props["isWin"]:
        output = output + "\nYOU WIN!"

    if game_state.props["isLoss"]:
        output = output + "\nGAME OVER."

    return output


def game_loop():
    # Initialize game
    game_state = GameState(make_board(10, 10, 10), {"isWin": False, "isLoss": False})
    print(render(game_state))

    while not any([game_state.props["isWin"], game_state.props["isLoss"]]):
        # Get user input
        jj = int(input("Enter row: "))
        ii = int(input("Enter column: "))

        # Update
        update((jj, ii), game_state)

        # Render
        print(render(game_state))


if __name__ == "__main__":
    random.seed(0)
    game_loop()
