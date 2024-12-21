"""Solve Advent of Code 2024, day 21

https://adventofcode.com/2024/day/21

+---+---+---+    +-----+-----+-----+
| 7 | 8 | 9 | -> | 3,2 | 3,1 | 3,0 |
+---+---+---+    +-----+-----+-----+
| 4 | 5 | 6 | -> | 2,2 | 2,1 | 2,0 |
+---+---+---+    +-----+-----+-----+
| 1 | 2 | 3 | -> | 1,2 | 1,1 | 1,0 |
+---+---+---+    +-----+-----+-----+
    | 0 | A | -> | 0,2 | 0,1 | 0,0 |
    +---+---+    +-----+-----+-----+

    +---+---+ -> +-----+-----+-----+
    | ^ | A | -> | 1,2 | 1,1 | 1,0 |
+---+---+---+ -> +-----+-----+-----+
| < | v | > | -> | 0,2 | 0,1 | 0,0 |
+---+---+---+ -> +-----+-----+-----+

All start at "A"

"""

import time

sequenceCache = {}

__PATHMAP__ = {
    ("A", "0"): "<A",
    ("0", "A"): ">A",
    ("A", "1"): "^<<A",
    ("1", "A"): ">>vA",
    ("A", "2"): "<^A",
    ("2", "A"): "v>A",
    ("A", "3"): "^A",
    ("3", "A"): "vA",
    ("A", "4"): "^^<<A",
    ("4", "A"): ">>vvA",
    ("A", "5"): "<^^A",
    ("5", "A"): "vv>A",
    ("A", "6"): "^^A",
    ("6", "A"): "vvA",
    ("A", "7"): "^^^<<A",
    ("7", "A"): ">>vvvA",
    ("A", "8"): "<^^^A",
    ("8", "A"): "vvv>A",
    ("A", "9"): "^^^A",
    ("9", "A"): "vvvA",
    ("0", "1"): "^<A",
    ("1", "0"): ">vA",
    ("0", "2"): "^A",
    ("2", "0"): "vA",
    ("0", "3"): "^>A",
    ("3", "0"): "<vA",
    ("0", "4"): "^<^A",
    ("4", "0"): ">vvA",
    ("0", "5"): "^^A",
    ("5", "0"): "vvA",
    ("0", "6"): "^^>A",
    ("6", "0"): "<vvA",
    ("0", "7"): "^^^<A",
    ("7", "0"): ">vvvA",
    ("0", "8"): "^^^A",
    ("8", "0"): "vvvA",
    ("0", "9"): "^^^>A",
    ("9", "0"): "<vvvA",
    ("1", "2"): ">A",
    ("2", "1"): "<A",
    ("1", "3"): ">>A",
    ("3", "1"): "<<A",
    ("1", "4"): "^A",
    ("4", "1"): "vA",
    ("1", "5"): "^>A",
    ("5", "1"): "<vA",
    ("1", "6"): "^>>A",
    ("6", "1"): "<<vA",
    ("1", "7"): "^^A",
    ("7", "1"): "vvA",
    ("1", "8"): "^^>A",
    ("8", "1"): "<vvA",
    ("1", "9"): "^^>>A",
    ("9", "1"): "<<vvA",
    ("2", "3"): ">A",
    ("3", "2"): "<A",
    ("2", "4"): "<^A",
    ("4", "2"): "v>A",
    ("2", "5"): "^A",
    ("5", "2"): "vA",
    ("2", "6"): "^>A",
    ("6", "2"): "<vA",
    ("2", "7"): "<^^A",
    ("7", "2"): "vv>A",
    ("2", "8"): "^^A",
    ("8", "2"): "vvA",
    ("2", "9"): "^^>A",
    ("9", "2"): "<vvA",
    ("3", "4"): "<<^A",
    ("4", "3"): "v>>A",
    ("3", "5"): "<^A",
    ("5", "3"): "v>A",
    ("3", "6"): "^A",
    ("6", "3"): "vA",
    ("3", "7"): "<<^^A",
    ("7", "3"): "vv>>A",
    ("3", "8"): "<^^A",
    ("8", "3"): "vv>A",
    ("3", "9"): "^^A",
    ("9", "3"): "vvA",
    ("4", "5"): ">A",
    ("5", "4"): "<A",
    ("4", "6"): ">>A",
    ("6", "4"): "<<A",
    ("4", "7"): "^A",
    ("7", "4"): "vA",
    ("4", "8"): "^>A",
    ("8", "4"): "<vA",
    ("4", "9"): "^>>A",
    ("9", "4"): "<<vA",
    ("5", "6"): ">A",
    ("6", "5"): "<A",
    ("5", "7"): "<^A",
    ("7", "5"): "v>A",
    ("5", "8"): "^A",
    ("8", "5"): "vA",
    ("5", "9"): "^>A",
    ("9", "5"): "<vA",
    ("6", "7"): "<<^A",
    ("7", "6"): "v>>A",
    ("6", "8"): "<^A",
    ("8", "6"): "v>A",
    ("6", "9"): "^A",
    ("9", "6"): "vA",
    ("7", "8"): ">A",
    ("8", "7"): "<A",
    ("7", "9"): ">>A",
    ("9", "7"): "<<A",
    ("8", "9"): ">A",
    ("9", "8"): "<A",

    ("<", "^"): ">^A",
    ("^", "<"): "v<A",
    ("<", "v"): ">A",
    ("v", "<"): "<A",
    ("<", ">"): ">>A",
    (">", "<"): "<<A",
    ("<", "A"): ">>^A",
    ("A", "<"): "v<<A",
    ("^", "v"): "vA",
    ("v", "^"): "^A",
    ("^", ">"): "v>A",
    (">", "^"): "<^A",
    ("^", "A"): ">A",
    ("A", "^"): "<A",
    ("v", ">"): ">A",
    (">", "v"): "<A",
    ("v", "A"): "^>A",
    ("A", "v"): "<vA",
    (">", "A"): "^A",
    ("A", ">"): "vA",
}

def getMoveCount(current, nxt, depth):
    """
    Holt die kürzeste Sequenz, um von 'current' nach 'nxt' zu wechseln (aus 'paths'),
    und gibt dann die Länge zurück, die benötigt wird, wenn wir diese Sequenz
    nochmal in getSequenceLength hineinstecken (mit depth-1).
    """
    # Falls identisch, return 1
    if current == nxt:
        return 1
    # Ansonsten LUT
    newSequence = __PATHMAP__.get((current, nxt), "")
    return getSequenceLength(newSequence, depth - 1)

def getSequenceLength(targetSequence, depth):
    """
    Kernfunktion, die rekursiv (bzw. kaskadierend) die "Kosten" berechnet.
    - depth=0 => Rückgabe: length = len(targetSequence)
    - depth>0 => Starte bei 'A', laufe durch targetSequence und summiere getMoveCount(...)
    Entspricht in Rust: getSequenceLength(...)
    """
    key = (targetSequence, depth)
    if key in sequenceCache:
        return sequenceCache[key]

    length = 0
    if depth == 0:
        # Rust: length = len(targetSequence)
        length = len(targetSequence)
    else:
        current = 'A'
        for nxt in targetSequence:
            length += getMoveCount(current, nxt, depth)
            current = nxt

    sequenceCache[key] = length
    return length

def calculateScore(code, robots):
    """
    Entspricht in Rust: calculateScore(code string, robots int) int
    """
    numericCode = int(code[:-1])
    length = getSequenceLength(code, robots)
    return numericCode * length

if __name__ == "__main__":
    sequences = ["140A", "143A", "349A", "582A", "964A"]
    # sequences = ["029A", "980A", "179A", "456A", "379A"]

    # Teil 1: "3 robots"
    solution1 = 0
    start_time = time.perf_counter()
    for code in sequences:
        solution1 += calculateScore(code, 3)
    print(
        f"Solution 1: {solution1} Computed in {time.perf_counter() - start_time:.5f} seconds."
    )

    # Teil 2: "26 robots"
    solution2 = 0
    start_time = time.perf_counter()
    for code in sequences:
        solution2 += calculateScore(code, 26)
    print(
        f"Solution 2: {solution2} Computed in {time.perf_counter() - start_time:.5f} seconds."
    )

    print(f"{solution1=} | {solution2=}")

