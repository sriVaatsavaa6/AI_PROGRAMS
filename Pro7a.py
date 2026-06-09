class FC:
    def __init__(self, rules, facts):
        self.rules = rules
        self.facts = set(facts)

    def apply(self):
        change = True
        while change:
            change = False
            for a, c in self.rules:
                if a.issubset(self.facts) and c not in self.facts:
                    self.facts.add(c)
                    change = True


rules = [
    ({"has_fur(tiger)"}, "mammal(tiger)"),
    ({"has_feathers(penguin)", "lays_eggs(penguin)"}, "bird(penguin)"),
    ({"lays_eggs(sparrow)", "has_feathers(sparrow)"}, "bird(sparrow)"),
    ({"has_fur(cat)"}, "mammal(cat)")
]

facts = {
    "has_fur(tiger)",
    "has_feathers(penguin)",
    "lays_eggs(penguin)",
    "lays_eggs(sparrow)",
    "has_fur(cat)"
}

fc = FC(rules, facts)
fc.apply()

print("Derived Facts:", fc.facts)
