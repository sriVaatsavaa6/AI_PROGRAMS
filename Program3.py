import heapq

class Node:
    def __init__(self, state, parent, action, cost, h):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.h = h

    def __lt__(self, other):
        return (self.cost + self.h) < (other.cost + other.h)

def astar(start, goal, graph):
    def h(s):
        return abs(ord(s) - ord(goal))

    frontier = [Node(start, None, None, 0, h(start))]
    explored = set()

    while frontier:
        node = heapq.heappop(frontier)

        if node.state == goal:
            path = []
            while node.parent:
                path.append((node.action, node.state))
                node = node.parent
            return path[::-1]

        explored.add(node.state)

        for neighbor, cost in graph.get(node.state, []):
            if neighbor not in explored:
                heapq.heappush(frontier, Node(neighbor, node, f"Move to {neighbor}",
                                               node.cost + cost, h(neighbor)))
    return None

graph = {}
n = int(input("Enter number of edges: "))

for _ in range(n):
    u, v, c = input("Enter edge (u v cost): ").split()
    c = int(c)
    graph.setdefault(u, []).append((v, c))
    graph.setdefault(v, []).append((u, c))

start = input("Enter start state: ")
goal = input("Enter goal state: ")

path = astar(start, goal, graph)

if path:
    print("Path found:")
    for action, state in path:
        print(action, "->", state)
else:
    print("No path found")
