"""Boggle word check.

Given a 5x5 boggle board, see if you can find a given word in it.

In Boggle, you can start with any letter, then move in any NEWS direction.
You can continue to change directions, but you cannot use the exact same
tile twice.

So, for example::

    N C A N E
    O U I O P
    Z Q Z O N
    F A D P L
    E D E A Z

In this grid, you could find `NOON* (start at the `N` in the top
row, head south, and turn east in the third row). You cannot find
the word `CANON` --- while you can find `CANO` by starting at the
top-left `C`, you can 't re-use the exact same `N` tile on the
front row, and there's no other `N` you can reach.

For example::

    >>> board = make_board('''
    ... N C A N E
    ... O U I O P
    ... Z Q Z O N
    ... F A D P L
    ... E D E A Z
    ... ''')

`NOON` should be found (0, 3) -> (1, 3) -> (2, 3) -> (2, 4)::

    >>> find(board, "NOON")
    True

`NOPE` should be found (0, 3) -> (1, 3) -> (1, 4) -> (0, 4)::

    >>> find(board, "NOPE")
    True

`CANON` can't be found (`CANO` starts at (0, 1) but can't find
the last `N` and can't re-use the N)::

    >>> find(board, "CANON")
    False

You cannot travel diagonally in one move, which would be required
to find `QUINE`::

    >>> find(board, "QUINE")
    False

We can recover if we start going down a false path (start 3, 0)::

    >>> find(board, "FADED")
    True


An extra tricky case --- it needs to find the `N` toward the top right,
and then go down, left, up, up, right to find all four `O`s and the `S`::

    >>> board2 = make_board('''
    ... E D O S Z
    ... N S O N R
    ... O U O O P
    ... Z Q Z O R
    ... F A D P L
    ... ''')

    >>> find(board2, "NOOOOS")
    True

"""


def make_board(board_string):
    """Make a board from a string.

    For example::

        >>> board = make_board('''
        ... N C A N E
        ... O U I O P
        ... Z Q Z O N
        ... F A D P L
        ... E D E A Z
        ... ''')

        >>> len(board)
        5

        >>> board[0]
        ['N', 'C', 'A', 'N', 'E']
    """

    letters = board_string.split()

    board = [
        letters[0:5],
        letters[5:10],
        letters[10:15],
        letters[15:20],
        letters[20:25],
    ]

    return board



def find(board, word):
    """Can word be found in board?"""
    rows, cols = len(board), len(board[0])

    def search(r, c, index, visited):
        """Recursively search for word starting at board[r][c]"""
        if index == len(word):
            return True # Base case: found word
        
        # Out of bounds, or already visited, or does not match current letter
        if (r < 0 or r >= rows or c < 0 or c >=cols or visited[r][c] or board[r][c] != word[index]):
            return False
        
        visited[r][c] = True  # mark this tile as visited

        # Explore all 4 NSEW directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            if search(r + dr, c + dc, index + 1, visited):
                return True
            
        # Backtrack and unmark tile as visited
        visited[r][c] = False
        return False
    
    # Find word from every tile on the board
    for r in range(rows):
        for c in range(cols):
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            if search(r, c, 0, visited):
                return True
            
    return False



if __name__ == '__main__':

    # Example tests
    board = make_board('''
    N C A N E
    O U I O P
    Z Q Z O N
    F A D P L
    E D E A Z
    ''')

    print(find(board, "NOON"))  # True
    print(find(board, "NOPE"))  # True
    print(find(board, "CANON")) # False
    print(find(board, "QUINE")) # False
    print(find(board, "FADED")) # True
    
    board2 = make_board('''
    E D O S Z
    N S O N R
    O U O O P
    Z Q Z O R
    F A D P L
    ''')

    print(find(board2, "NOOOOS"))  # True


    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; YOU FOUND SUCCESS! ***\n")
