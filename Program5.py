def queens(n=8):
    sols = []
    def bt(cols, d1, d2, p):
        r = len(p)
        if r == n:
            sols.append(p[:])
            return
        for c in range(n):
            if c not in cols and (r-c) not in d1 and (r+c) not in d2:
                bt(cols | {c}, d1 | {r-c}, d2 | {r+c}, p + [c])
    bt(set(), set(), set(), [])
    return sols

sols = queens()
print(f"Total:{len(sols)}\n")

for i, s in enumerate(sols[:2], 1):
    print(f"Solution {i}:{s}")
    for r in range(8):
        print(''.join('Q' if c == s[r] else '.' for c in range(8)))
    print()
