import heapq

class Node:
    def __init__(self, s, p=None, a=None, c=0, h=0):
        self.s, self.p, self.a, self.c, self.h = s, p, a, c, h
    def __lt__(self, o):
        return (self.c + self.h) < (o.c + o.h)

def h(s):
    return {'A':5,'B':3,'C':2,'D':1,'E':2,'G':0}.get(s, float('inf'))

def ao_star(start, goal, g):
    pq, vis = [Node(start, None, None, 0, h(start))], {}

    while pq:
        n = heapq.heappop(pq)
        if n.s == goal:
            path = []
            while n.p:
                path.append((n.a, n.s))
                n = n.p
            return path[::-1]

        if n.s not in vis or n.c < vis[n.s]:
            vis[n.s] = n.c
            for nb, c in g.get(n.s, []):
                heapq.heappush(pq, Node(nb, n, f"Move to {nb}", n.c+c, h(nb)))
    return None

g = {}
for _ in range(int(input("Enter the number of edges: "))):
    u, v, c = input("Enter an edge (format: u v cost): ").split()
    g.setdefault(u, []).append((v, float(c)))
    g.setdefault(v, [])

start = input("Enter the start state: ")
goal = input("Enter the goal state: ")

res = ao_star(start, goal, g)
if res:
    print("Path found:")
    for a, s in res:
        print(f"Action: {a}, State: {s}")
else:
    print("No path found.")
