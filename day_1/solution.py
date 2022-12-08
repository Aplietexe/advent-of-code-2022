from pathlib import Path

inp = (Path(__file__).parent / "input.txt").open().read()

s = [sum(int(food) for food in foods.split("\n")) for foods in inp.split("\n\n")]

p1 = max(s)

p2 = sum(sorted(s, reverse=True)[:3])

print(p1, p2)
