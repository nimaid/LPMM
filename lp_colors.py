BLACK = 0
DARK_GREY = 1
GREY = 2
WHITE = 3
RED = 5
RED_HALF = 6
RED_THIRD = 7
AMBER = 9
AMBER_HALF = 10
AMBER_THIRD = 11
GREEN = 21
GREEN_HALF = 22
GREEN_THIRD = 23
YELLOW = 13
YELLOW_HALF = 14
YELLOW_THIRD = 15
MINT = 29
MINT_HALF = 30
MINT_THIRD = 31
LIGHT_BLUE = 37
LIGHT_BLUE_HALF = 38
LIGHT_BLUE_THIRD = 39
BLUE = 45
BLUE_HALF = 46
BLUE_THIRD = 47
PINK = 53
PINK_HALF = 54
PINK_THIRD = 55
PURPLE = 48
PURPLE_HALF = 49
PURPLE_THIRD = 50

curr_colors = [[BLACK for y in range(9)] for x in range(9)]
effect_colors = [[GREEN for y in range(9)] for x in range(9)]

import lp_events

lp_object = None

def init(lp_object_in):
    global lp_object
    lp_object = lp_object_in
                

def setXY(x, y, color):
    curr_colors[x][y] = color

def effectXY(x, y, color):
    effect_colors[x][y] = color

def getXY(x, y):
    return curr_colors[x][y]

def update():
    for x in range(8): #top funcs
        set_color = None
        if lp_events.pressed[x][0]:
            set_color = effect_colors[x][0]
        else:
            set_color = curr_colors[x][0]
        lp_object.LedCtrlXYByCode(x, 0, set_color)

    for y in range(1, 9):
        set_color = None
        if lp_events.pressed[8][y]:
            set_color = effect_colors[8][y]
        else:
            set_color = curr_colors[8][y]
        lp_object.LedCtrlXYByCode(8, y, set_color)

    for x in range(8):
        for y in range(1, 9):
            set_color = None
            if lp_events.pressed[x][y]:
                set_color = effect_colors[x][y]
##                if lp_events.mode == "INSTRUMENT":
##                    if lp_instrument.working_notes[x][y] in lp_midi.curr_notes:
##                        set_color = lp_instrument.ACTIVE
            else:
                set_color = curr_colors[x][y]
            lp_object.LedCtrlXYByCode(x, y, set_color)
