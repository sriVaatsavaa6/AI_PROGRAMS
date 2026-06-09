class BC:
    def __init__(self, r, f):
        self.r = r
        self.f = set(f)

    def check(self, x):
        if x in self.f:
            return True
        for a, c in self.r:
            if c == x and all(self.check(i) for i in a):
                return True
        return False


rules = [
    ({"has_fur(tiger)"}, "mammal(tiger)"),
    ({"has_feathers(penguin)", "lays_eggs(penguin)"}, "bird(penguin)")
]

facts = {
    "has_fur(tiger)",
    "has_feathers(penguin)",
    "lays_eggs(penguin)"
}

goals = ["mammal(tiger)", "bird(penguin)"]

bc = BC(rules, facts)

for g in goals:
    if bc.check(g):
        print(f"Goal {g} can be derived from the facts.")
    else:
        print(f"Goal {g} cannot be derived from the facts.")
