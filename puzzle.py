from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    # a is a knave or a knight
    Or(AKnight, AKnave),
    # a is not both a knave and a knight
    Not(And(AKnight, AKnave)),
    # if a is a knight
    Implication(AKnight, And(AKnight, AKnave)),
    # if a is a knave
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    # a is a knave or a knight
    Or(AKnight, AKnave),
    # a is not both a knave and a knight
    Not(And(AKnight, AKnave)),
    # b is a knave or a knight
    Or(BKnight, BKnave),
    # b is not both a knave and a knight
    Not(And(BKnight, BKnave)),

    # if a is a knave
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    # a is a knave or a knight
    Or(AKnight, AKnave),
    # a is not both a knave and a knight
    Not(And(AKnight, AKnave)),
    # b is a knave or a knight
    Or(BKnight, BKnave),
    # b is not both a knave and a knight
    Not(And(BKnight, BKnave)),

    # if a is a knave
    Implication(AKnave, Not(And(AKnave, BKnave))),
    # if a is a knight
    Implication(AKnight, And(AKnight, BKnight)),
    # if b is a knight
    Implication(BKnight, Not(And(AKnight, BKnight))),
    # if b is a knave
    Implication(BKnave, And(AKnave, BKnave))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    Not(And(AKnight, AKnave)),  # A cannot be knight and knave at the same time
    Or(AKnight, AKnave),  # A will be Knight or Knave

    Not(And(BKnight, BKnave)),  # B cannot be knight and knave at the same time
    Or(BKnight, BKnave),  # B will be Knight or Knave

    Not(And(CKnight, CKnave)),  # C cannot be knight and knave at the same time
    Or(CKnight, CKnave),  # C will be Knight or Knave

    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Or(
        # "I am a knight."
        And(
            Implication(AKnight, AKnight),
            Implication(AKnave, Not(AKnight))
        ),

        # "I am a knave."
        And(
            Implication(AKnight, AKnave),
            Implication(AKnave, Not(AKnave))
        )
    ),

    Not(And(
        # "I am a knight."
        And(
            Implication(AKnight, AKnight),
            Implication(AKnave, Not(AKnight))
        ),

        # "I am a knave."
        And(
            Implication(AKnight, AKnave),
            Implication(AKnave, Not(AKnave))
        )
    )),

    # B says "A said 'I am a knave'."
    Implication(BKnight, And(
        Implication(AKnight, AKnave),
        Implication(AKnave, Not(AKnave))
    )),

    Implication(BKnave, Not(And(
        Implication(AKnight, AKnave),
        Implication(AKnave, Not(AKnave))
    ))),

    # B says "C is a knave."
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # C says "A is a knight."
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
