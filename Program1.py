def water_jug(j1_cap, j2_cap, target):
    visited = set()

    def dfs(j1, j2):
        if (j1, j2) in visited:
            return False

        visited.add((j1, j2))

        # Only accept when Jug 1 has target and Jug 2 is empty
        if j1 == target and j2 == 0:
            print(f"Jug 1 now has {target} liters.")
            return True

        # All 6 operations
        ops = [
            ('Fill Jug 1', j1_cap, j2),
            ('Fill Jug 2', j1, j2_cap),
            ('Empty Jug 1', 0, j2),
            ('Empty Jug 2', j1, 0),
            ('Pour Jug 1 to Jug 2', max(0, j1+j2-j2_cap), min(j2_cap, j1+j2)),
            ('Pour Jug 2 to Jug 1', min(j1_cap, j1+j2), max(0, j1+j2-j1_cap))
        ]

        for action, new_j1, new_j2 in ops:
            if (new_j1, new_j2) not in visited:
                print(f"Trying: {action} => ({new_j1}, {new_j2})")
                if dfs(new_j1, new_j2):
                    return True

        return False

    if dfs(0, 0):
        print("Solution found!")
    else:
        print("Solution not possible.")

# Input
j1_cap = int(input("Enter Jug 1 capacity : "))
j2_cap = int(input("Enter Jug 2 capacity : "))
target = int(input("Enter Target Volume : "))

print(f"Solving Water Jug Problem with capacities ({j1_cap}, {j2_cap}) to measure {target} liters.")
water_jug(j1_cap, j2_cap, target)
