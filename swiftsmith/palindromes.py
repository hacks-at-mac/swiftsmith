from grammar import Nonterminal, PProduction, PCFG

S = Nonterminal("START")

palindrome = PCFG(
    S,
    [
        PProduction(S, ["a", S, "a"], 0.4),
        PProduction(S, ["b", S, "b"], 0.5),
        PProduction(S, ["c"], 0.1),
    ]
)

tree = palindrome.randomtree()
print(tree.string())
