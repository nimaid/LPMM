import copy, threading, time
import lp_colors

RUN_DELAY = 0.01

def nop():
    return None

press_funcs = [[nop for y in range(9)] for x in range(9)]
release_funcs = copy.deepcopy(press_funcs)

timer = None

def init(lp_object):
    global timer
    timer = threading.Timer(RUN_DELAY, run, [lp_object])

def run(lp_object):
    global timer
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
    init(lp_object)
    timer.start()

def start(lp_object):
    init(lp_object)
    run(lp_object)

