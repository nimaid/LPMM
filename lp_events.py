import copy, threading, time
import lp_colors, lp_instrument

RUN_DELAY = 0.005 #0.005 == 200 FPS

def unbound_press(x, y):
    print("[LPMM] UNBOUND BUTTON ("+str(x)+", "+str(y)+") DOWN\n>>> ", end = "")

def unbound_release(x, y):
    print("[LPMM] UNBOUND BUTTON ("+str(x)+", "+str(y)+") UP\n>>> ", end = "")

press_funcs = [[unbound_press for y in range(9)] for x in range(9)]
release_funcs = [[unbound_release for y in range(9)] for x in range(9)]

pressed = [[False for y in range(9)] for x in range(9)]

timer = None
mode = "INSTRUMENT"

def init(lp_object):
    global timer
    timer = threading.Timer(RUN_DELAY, run, [lp_object])

def run(lp_object):
    global timer
    while True:
        event = lp_object.ButtonStateXY()
        if event != []:
            if event[2] == 0:
                pressed[event[0]][event[1]] = False
                release_funcs[event[0]][event[1]](event[0], event[1])
            else:
                pressed[event[0]][event[1]] = True
                press_funcs[event[0]][event[1]](event[0], event[1])
        else:
            break
    init(lp_object)
    timer.start()

def start(lp_object):
    lp_colors.init(lp_object)
    init(lp_object)
    run(lp_object)
    lp_instrument.bind_grid()
    lp_instrument.bind_function_keys()
    lp_colors.update()

def bind_func_with_colors(x, y, func, off_color, on_color = lp_colors.GREEN, release_func = None):
    global press_funcs
    if release_func == None:
        release_func = lambda a, b : None
    press_funcs[x][y] = func
    release_funcs[x][y] = release_func
    lp_colors.setXY(x, y, off_color)
    lp_colors.effectXY(x, y, on_color)

def unbind_all():
    global press_funcs
    global release_funcs
    press_funcs = [[unbound_press for y in range(9)] for x in range(9)]
    release_funcs = [[unbound_release for y in range(9)] for x in range(9)]
    for x in range(9):
        for y in range(9):
            lp_colors.setXY(x, y, lp_colors.BLACK)
            lp_colors.effectXY(x, y, lp_colors.BLACK)
    lp_colors.update()
