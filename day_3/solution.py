from pathlib import Path

inp = (Path(__file__).parent / "input.txt").open().read()

s = [(i[: len(i) // 2], i[-len(i) // 2 :]) for i in inp.splitlines()]

r = ""

for a, b in s:
    for l in a:
        if l in b:
            r += l
            break

print(sum(ord(i) - 96 if ord(i) >= 97 else ord(i) - 38 for i in r))

r = ""
s = inp.splitlines()

for i, l in enumerate(s):
    if i % 3 != 0:
        continue

    for x in l:
        if x in s[i + 1] and x in s[i + 2]:
            r += x
            break


print(sum(ord(i) - 96 if ord(i) >= 97 else ord(i) - 38 for i in r))
