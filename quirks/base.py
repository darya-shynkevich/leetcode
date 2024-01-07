print(next(iter({1: 11, 2: 22})))

print(type({}))

print(type({0}))

print(type(True))

print(isinstance(True, int))

print(isinstance(True, bool))

print(type(1))

print(isinstance(1, int))

print(isinstance(1, bool))

print(all([]))

print(any([]))

print("qwe" * True)

print([*[1, 2, 3], *[4, 5, 6]])

x = 5; print(f"{x=}")

print(["qwe" "rty"])

print([] + [])

print(1 + 1.1)

print("qwe" + "rty")

print(False + 1)

print([] < "")

print([] < 0)

print("qwe" + 1)

x = 1; y = 20; x, y = y, x
print(x, y)

print(len("Python"))

print(bool([]))

print(bool(""))

print(bool(0))

print(bool(None))

print(1 / 0)

print(int("123"))

print(float("3.14"))

print(str(123))

print("Python"[2:])

print("Python"[:-2])

print("Python"[1:4:2])

print(type(range(5)))

print(list(range(5)))

print(sum(range(5)))

print(sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], reverse=True))

print([x**2 for x in range(5)])

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

print(dict([(1, 'one'), (2, 'two'), (3, 'three')]))

print(len({'one': 1, 'two': 2, 'three': 3}))

print(set([1, 2, 3, 1, 2, 3]))

print({'one', 'two', 'three'} & {'two', 'three', 'four'})

print({'one', 'two', 'three'} - {'two', 'three', 'four'})

print({'one', 'two', 'three'} | {'two', 'three', 'four'})
