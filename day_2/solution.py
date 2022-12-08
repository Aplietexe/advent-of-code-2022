from pathlib import Path

inp = (Path(__file__).parent / "input.txt").open().read()

t = 0

for l in inp.splitlines():
    o, p = l.split(" ")

    o = ord(o) - ord("A")
    p = ord(p) - ord("X")

    if o == p:
        t += 3
    elif (p - o) % 3 == 1:
        t += 6

    t += p + 1

print(t)

t = 0

for l in inp.splitlines():
    o, r = l.split(" ")

    o = ord(o) - ord("A")
    r = ord(r) - ord("X")

    if r == 0:
        t += (o - 1) % 3 + 1

    elif r == 1:
        t += 3 + o + 1
    else:
        t += 6 + (o + 1) % 3 + 1

print(t)
