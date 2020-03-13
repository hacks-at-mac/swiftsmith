from grammar import Nonterminal, PProduction, PCFG

# Noun, Verb, Determiner, Noun
# This is a pen.

# Subject Verb
# Noun, Verb, Adjective, Noun
# She sells sea shells.

# Noun, Verb, Noun
# I am bread.

# Verb, Preposition, Noun
# Welcome to MacHack.



S = Nonterminal("SENTENCE")

np = Nonterminal("NOUN_PHRASE")
vp = Nonterminal("VERB_PHRASE")
pp = Nonterminal("PREPOSITIONAL_PHRASE")

noun = Nonterminal("NOUN")
verb = Nonterminal("VERB")
det = Nonterminal("DETERMINER")
adj = Nonterminal("ADJECTIVE")
p = Nonterminal("PREPOSITION")

english = PCFG(
    S,
    [
        PProduction(S, [np, vp], 0.75),
        #PProduction(S, [vp], 0.25),

        PProduction(np, [noun], 0.5),
        PProduction(np, [det, noun], 0.2),
        PProduction(np, [adj, noun], 0.2),
        PProduction(np, [np, pp], 0.05),
        
        PProduction(vp, [verb], 0.4),
        PProduction(vp, [verb, np], 0.5),
        PProduction(vp, [vp, pp], 0.1),

        PProduction(pp, [p, np], 1.0),

        PProduction(noun, ["pen"], 0.1),
        PProduction(noun, ["shell"], 0.1),
        PProduction(noun, ["MacHack"], 0.1),
        PProduction(noun, ["bread"], 0.1),

        PProduction(verb, ["is"], 0.25),
        PProduction(verb, ["sells"], 0.25),
        PProduction(verb, ["welcomes"], 0.25),
        PProduction(verb, ["eats"], 0.25),
        PProduction(verb, ["practices"], 0.25),
        PProduction(verb, ["runs"], 0.25),

        PProduction(det, ["a"], 0.5),
        PProduction(det, ["this"], 0.5),

        PProduction(adj, ["tall"], 0.25),
        PProduction(adj, ["short"], 0.25),
        PProduction(adj, ["tasty"], 0.25),
        PProduction(adj, ["fabulous"], 0.25),
        PProduction(adj, ["bready"], 0.25),

        PProduction(p, ["to"], 1.0),
    ]
)

tree = english.randomtree()
print(tree.string())
