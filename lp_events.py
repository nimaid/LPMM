import copy
import lp_colors

def nop():
    return None

press_funcs = [[nop for y in range(9)] for x in range(9)]
release_funcs = copy.deepcopy(press_funcs)

def run(lp_object):
    while True:
        event = lp_object.ButtonStateXY()
        if event != []:
            if event[2] == 0:
                old_color = lp_colors.curr_colors[event[0]][event[1]]
                lp_object.LedCtrlXYByCode(event[0], event[1], old_color)
                release_funcs[event[0]][event[1]]()
            else:
                lp_object.LedCtrlXYByCode(event[0], event[1], lp_colors.GREEN)
                press_funcs[event[0]][event[1]]()
        else:
            break


