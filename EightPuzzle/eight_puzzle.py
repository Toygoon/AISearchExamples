class EightPuzzle:
    """
    Author: Toygoon

    This class represents the 8-puzzle game board and provides methods for managing game state.
    """

    # Define directions as a class-level variable.
    DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def __init__(self, board):
        """
        Initialize the game board with the provided board state.
        """
        self.board = board

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
        pass

    def solved(self) -> bool:
        """
        Check whether the current game board state is the solved state.
        The solved state is when the tiles are in the following order:

        Returns:
            bool: True if the board is solved, False otherwise.
        """
        # Solved check implementation
        pass

    def scramble(self):
        """
        Scramble the game board by making a random sequence of tile moves.
        This method modifies the game board in place.
        """
        # Scramble board implementation
        pass
