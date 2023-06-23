import collections


def isValidSoduko(board):
    """
    Optimal time complexity: O(n^2) = O(9^2)
        Algorithm:
            - Make 3 hashmaps for row, column and subgrid each with default sets if you try to access keys
            - run through the entire grid and check if the elements are already in one of the sets in three hashmaps
            - label the subgrid with a tuple that contains the row and column // 3 (integer division)
        Corresponding space complexity: O(n^2)
    :param board:
    :return:
    """
    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    subgrids = collections.defaultdict(set)

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '.':
                continue
            if (board[row][col] in rows[row] or board[row][col] in columns[col] \
            or board[row][col] in subgrids[(row // 3, col // 3)]):
                return False
            else:
                rows[row].add(board[row][col])
                columns[col].add(board[row][col])
                subgrids[(row//3,col//3)].add(board[row][col])
    return True

