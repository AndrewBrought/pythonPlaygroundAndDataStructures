"""
Python Data Structures - A Game-Based Approach
DFS maze solver.
Robin Andrews - https://compucademy.net/
The stack contains positions as (row, column) tuples. Predecessors are kept in a dictionary.
"""
from helpers import get_path, offsets, is_legal_pos, read_maze
from stack import Stack


def dfs(maze, start, goal):
    # We instantiate a new stack
    stack = Stack()
    # We're pushing our start position which is a coordinate/row, column tuples (an immutable list)
    stack.push(start)
    #     predecessors is a dictionary containing the predecessor of the start position, which is none
    predecessors = {start: None}

    while not stack.is_empty():
        # While the stack is not empty, we get the current cell by popping
        current_cell = stack.pop()
        # We check if it's the goal, if it is, the program is finished!
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        # Otherwise, for every direction in this list, we check the offsets (imported from helper
        # file and we assign the i, j values from from that so that we can then check the neighbor
        # The whole point of this is to check the coordinates of the contiguous cells in all four directions
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            # neighbor refers to the cell
            neighbor = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            # now we say, for each of those directions, if it's a legal position and it doesn't already exist in our
            # predecessors list, that means we haven't discovered it yet - so we push it on to our stack.
            if is_legal_pos(maze, neighbor) and neighbor not in predecessors:
                # finally we push the neighbor on the stack and update the predecessors
                stack.push(neighbor)
                predecessors[neighbor] = current_cell
    return None


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_dfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_dfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = dfs(maze, start_pos, goal_pos)
    assert result is None
