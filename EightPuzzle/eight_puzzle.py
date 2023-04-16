class EightPuzzle:
    """
    Author: Toygoon

    This class represents the 8-puzzle game board and provides methods for managing game state.
    """

    # Define directions as a class-level variable.
    DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def __init__(self, board, func):
        """
        Initialize the game board with the provided board state.

        Args:
            board (list): The game board state as a 2D list.
            func (function): The search function to use for solving the puzzle.
        """
        self.board = board
        self.func = func

    def move(self, row, col) -> bool:
        """
        Move the tile at the given row and column to the empty space.
        This method updates the game board by swapping the positions of the tiles.

        Args:
            row (int): The row index of the tile to move.
            col (int): The column index of the tile to move.

        Returns:
            bool: True if the tile was successfully moved, False otherwise.
        """
        # Find the location of the empty space
        empty_row, empty_col = self.find(0)
        for d in self.DIRS:
            # Calculate new directions
            new_row, new_col = row + d[0], col + d[1]

            # Check if the move is valid
            if new_row == empty_row and new_col == empty_col:
                # Swap the positions of the tiles
                self.board[row][col], self.board[empty_row][empty_col] = \
                    self.board[empty_row][empty_col], self.board[row][col]

                # Return True to indicate a successful move
                return True

        return False

    def solved(self) -> bool:
        """
        Check whether the current game board state is the solved state.
        The solved state is when the tiles are in the following order:

        Returns:
            bool: True if the board is solved, False otherwise.
        """
        # The goal state is a 3x3 grid with the numbers 1 to 8 in increasing order,
        # with a blank space at the bottom-right corner.
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

        # Compare the current board state with the goal state.
        return self.board == goal

    def scramble(self):
        """
        Scramble the game board by making a random sequence of tile moves.
        This method modifies the game board in place.
        """
        # Scramble board implementation
        pass
