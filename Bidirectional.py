# Problem statement: We are trying to find the shortest path between two points on a simple grid using the bidirectional search algorithm


from collections import deque
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
        results = filter(self.in_bounds, results)
        return results

# Bidirectional BFS algorithm
def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    visited_from_start = {start}
    visited_from_goal = {goal}

    parent_from_start = {start: None}
    parent_from_goal = {goal: None}

    queue_from_start = deque([start])
    queue_from_goal = deque([goal])

    while queue_from_start and queue_from_goal:
        if queue_from_start:
            current = queue_from_start.popleft()
            for next in graph.neighbors(current):
                if next not in visited_from_start:
                    queue_from_start.append(next)
                    visited_from_start.add(next)
                    parent_from_start[next] = current
                    if next in visited_from_goal:
                        return reconstruct_path(parent_from_start, parent_from_goal, next)

        if queue_from_goal:
            current = queue_from_goal.popleft()
            for next in graph.neighbors(current):
                if next not in visited_from_goal:
                    queue_from_goal.append(next)
                    visited_from_goal.add(next)
                    parent_from_goal[next] = current
                    if next in visited_from_start:
                        return reconstruct_path(parent_from_start, parent_from_goal, next)

    return None

def reconstruct_path(parent_from_start, parent_from_goal, meeting_point):
    path = [meeting_point]
    while parent_from_start[path[0]] is not None:
        path.insert(0, parent_from_start[path[0]])
    while parent_from_goal[path[-1]] is not None:
        path.append(parent_from_goal[path[-1]])
    return path

# Create a grid and define start and goal
grid = Grid(10, 10)  # 10x10 grid
start = (0, 0)  # Top-left corner
goal = (7, 7)  # Some arbitrary point

# Find the path using bidirectional search
path = bidirectional_search(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found.")
