import copy

def nop():
    return None

press_funcs = []
for x in range(9):
    press_funcs.append([])
    for y in range(9):
        if not (x == 0 and y == 8):
            press_funcs[x].append(nop)

release_funcs = copy.deepcopy(press_funcs)

def run(lp_object):
    while True:
        event = lp_object.ButtonStateXY()
        if event != []:
            if event[2] == 0:
                release_funcs[event[0]][event[1]]()
            else:
                press_funcs[event[0]][event[1]]()
        else:
            break


