from queue import PriorityQueue

class State:
    def __init__(self, left_m, left_c, boat, right_m, right_c):
        self.left_m = left_m
        self.left_c = left_c
        self.boat = boat
        self.right_m = right_m
        self.right_c = right_c

    def is_valid(self):
        if self.left_m < 0 or self.left_c < 0 or self.right_m < 0 or self.right_c < 0:
            return False
        if self.left_m > 0 and self.left_c > self.left_m:
            return False
        if self.right_m > 0 and self.right_c > self.right_m:
            return False
        return True

    def is_goal(self):
        return self.left_m == 0 and self.left_c == 0

    def __lt__(self, other):
        return False

    def __eq__(self, other):
        return (self.left_m, self.left_c, self.boat, self.right_m, self.right_c) == \
               (other.left_m, other.left_c, other.boat, other.right_m, other.right_c)

    def __hash__(self):
        return hash((self.left_m, self.left_c, self.boat, self.right_m, self.right_c))

def successors(state):
    succ = []
    direction = -1 if state.boat == 1 else 1

    for m in range(3):
        for c in range(3):
            if 1 <= m + c <= 2:
                new_state = State(
                    state.left_m + direction * m,
                    state.left_c + direction * c,
                    1 - state.boat,
                    state.right_m - direction * m,
                    state.right_c - direction * c
                )
                if new_state.is_valid():
                    succ.append(new_state)
    return succ

def best_first_search():
    start = State(3, 3, 1, 0, 0)
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost = {start: 0}

    while not frontier.empty():
        _, current = frontier.get()

        if current.is_goal():
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for next_state in successors(current):
            new_cost = cost[current] + 1
            if next_state not in cost or new_cost < cost[next_state]:
                cost[next_state] = new_cost
                frontier.put((new_cost, next_state))
                came_from[next_state] = current
    return None

def print_solution(path):
    if not path:
        print("No solution found.")
    else:
        print("Solution found!")
        for i, s in enumerate(path):
            print(f"Step {i}:")
            print(f"Left Bank: {s.left_m} missionaries, {s.left_c} cannibals")
            print(f"Boat is {'on the left' if s.boat == 1 else 'on the right'} bank")
            print(f"Right Bank: {s.right_m} missionaries, {s.right_c} cannibals")
            print("------------")

solution_path = best_first_search()
print_solution(solution_path)
