import copy, threading, time
import lp_colors

RUN_DELAY = 0.01

def unbound_press(x, y):
    print("[UNBOUND BUTTON ("+str(x)+", "+str(y)+") PRESS] Doing nothing...\n>>> ", end = "")

def unbound_release(x, y):
    print("[UNBOUND BUTTON ("+str(x)+", "+str(y)+") RELEASE] Doing nothing...\n>>> ", end = "")

press_funcs = [[unbound_press for y in range(9)] for x in range(9)]
release_funcs = [[unbound_release for y in range(9)] for x in range(9)]

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
                lp_colors.off_effect(event[0], event[1])
                release_funcs[event[0]][event[1]](event[0], event[1])
            else:
                lp_colors.on_effect(event[0], event[1])
                press_funcs[event[0]][event[1]](event[0], event[1])
        else:
            break
    init(lp_object)
    timer.start()

def start(lp_object):
    lp_colors.init(lp_object)
    init(lp_object)
    run(lp_object)

