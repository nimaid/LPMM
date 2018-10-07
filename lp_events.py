import copy, threading, time
import lp_colors, lp_instrument

RUN_DELAY = 0.005 #0.005 == 200 FPS

def unbound_press(x, y):
    print("[UNBOUND BUTTON ("+str(x)+", "+str(y)+") PRESS] Doing nothing...\n>>> ", end = "")

def unbound_release(x, y):
    print("[UNBOUND BUTTON ("+str(x)+", "+str(y)+") RELEASE] Doing nothing...\n>>> ", end = "")

press_funcs = [[unbound_press for y in range(9)] for x in range(9)]
release_funcs = [[unbound_release for y in range(9)] for x in range(9)]

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
            if mode == "INSTRUMENT":
                if lp_instrument.working_notes[8 - event[1]][event[0]] != None:
                    same_note = lp_instrument.get_keys_bound_to_same_note_as(event[0], event[1] - 1)
                    if event[2] == 0:
                        for n in same_note:
                            lp_colors.off_effect(n[0], n[1] + 1)
                        
                        release_funcs[event[0]][event[1]](event[0], event[1])
                    else:
                        for n in same_note:
                            lp_colors.on_effect(n[0], n[1] + 1)
                    
                        press_funcs[event[0]][event[1]](event[0], event[1])
                else:
                    if event[2] == 0:
                        lp_colors.off_effect(event[0], event[1])
                        release_funcs[event[0]][event[1]](event[0], event[1])
                    else:
                        lp_colors.on_effect(event[0], event[1])
                        press_funcs[event[0]][event[1]](event[0], event[1])
            else:
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
    lp_instrument.update()
    lp_instrument.bind_function_keys()

def bind_func_with_colors(x, y, func, off_color, on_color = lp_colors.GREEN, release_func = None):
    global press_funcs
    if release_func == None:
        release_func = lambda x, y : None
    press_funcs[x][y] = func
    release_funcs[x][y] = release_func
    lp_colors.setXY(x, y, off_color)
    lp_colors.effect_colors[x][y] = on_color
