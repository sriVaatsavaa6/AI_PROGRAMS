def tsp(d):
    n = len(d)
    tour, visited = [0], [0]
    cost = cur = 0

    while len(visited) < n:
        nxt = min((d[cur][i], i) for i in range(n) if i not in visited)[1]
        cost += d[cur][nxt]
        tour.append(nxt)
        visited.append(nxt)
        cur = nxt

    cost += d[cur][0]
    tour.append(0)

    return tour, cost


d = [
    [0, 4, 8, 9, 12],
    [4, 0, 6, 8, 9],
    [8, 6, 0, 10, 11],
    [9, 8, 10, 0, 7],
    [12, 9, 11, 7, 0]
]

tour, cost = tsp(d)

print("Nearest Neighbor TSP Tour:", tour)
print("Total Distance:", cost)
