def findCircleNum(self, M: List[List[int]]) -> int: \
    for row_index, row in enumerate(M):
        for col_index, digit in enumerate(row):
            if digit == 1:
                # lets look in all the surrounding directions
                counter += 1
                M[row_index][col_index] = 0
                # were setting equal to 0 b/c we don't want to double search this area we have already search through it
                # were interested in finding the connections/edges associated at that particular position
                # were to use a queue to search over the cardinal directions (up, down, left, right)
                # Use a queue to explore neightbors

                queue = deque((row_index, col_index))
                while len(queue) > 0:
                    # up
                    # were doing so that
                    r, c = queue.popleft()  # to empty the quue, and ulimately make the loop stop, we could have a situtation whhere there no neightboors

                    # up
                    if r > 0 and grid[r - 1][c] == '1':
                        grid[r - 1][c] = 0
                        queue.append((r - 1, c))

                    # down
                    if r < len(grid) - 1 and grid[r + 1][c] == '1':
                        grid[r + 1][c] = 0
                        queue.append((r + 1, c))

                    # left
                    if c < len(row) - 1 and grid[r][c + 1] == '1':
                        grid[r][c + 1] = 0
                        queue.append((r, c + 1))

                    # right
                    if c > 0 and grid[r][c - 1] == '1':
                        grid[r][c - 1] = 0
                        queue.append((r, c - 1))

    return counter