def neg(x):
    return x[1:] if x[0] == "~" else "~" + x

def resolution(kb):
    clauses = [c.replace("(", "").replace(")", "").split(" || ") for c in kb]

    while True:
        new = []

        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):

                for x in clauses[i]:
                    if neg(x) in clauses[j]:

                        r = list(set(clauses[i] + clauses[j]))
                        r.remove(x)
                        r.remove(neg(x))

                        if r not in clauses and r not in new:
                            new.append(r)

        if not new:
            return "Satisfiable"

        clauses += new


kb = [
    "(P || Q || ~R)",
    "(~P || R)",
    "(~Q || R)",
    "(~R || ~P || Q)"
]

print(resolution(kb))
