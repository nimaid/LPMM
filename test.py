import copy

empty = []
for x in range(2):
    empty.append([])
    for y in range(2):
        empty[x].append(False)

status = {k:[] for k in ["a", "b", "c"]}

status["a"] = copy.deepcopy(empty)
status["b"] = copy.deepcopy(empty)
status["c"] = copy.deepcopy(empty)


print(status)
status["a"][0][0] = True
print(status)
