BLACK = 0
WHITE_THIRD = 1
WHITE_HALF = 2
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
LIGHTBLUE = 37
LIGHTBLUE_HALF = 38
LIGHTBLUE_THIRD = 39
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
effect_colors = [[BLACK for y in range(9)] for x in range(9)]

import lp_events, lp_instrument, lp_midi, lp_scaleedit

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
    for x in range(8):
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

    if lp_events.mode == "INSTRUMENT":
        for x in range(8):
            for y in range(1, 9):
                set_color = None
                if lp_instrument.working_notes[y-1][x] in lp_midi.curr_notes:
                    set_color = lp_instrument.COLOR_EFFECT
                else:
                    set_color = curr_colors[x][y]
                lp_object.LedCtrlXYByCode(x, y, set_color)
    elif lp_events.mode == "SCALEEDIT":
        for x in range(8):
            for y in range(1, 9):
                set_color = None
                if lp_scaleedit.active[x][y] or lp_events.pressed[x][y]:
                    set_color = effect_colors[x][y]
                else:
                    set_color = curr_colors[x][y]
                lp_object.LedCtrlXYByCode(x, y, set_color)

update_bindable = lambda x, y : update()

# Just for fun, use lp_colors.rainbowreplace(lp_colors.LIGHTBLUE) in instrument mode ;)
def rainbow_replace(replace_color):
    for x in range(8):
        for y in range(1, 9):
            if curr_colors[x][y] == replace_color:
                rainbow_color = None
                if y == 1:
                    rainbow_color = PINK_THIRD
                elif y == 2:
                    rainbow_color = RED_THIRD
                elif y == 3:
                    rainbow_color = AMBER_THIRD
                elif y == 4:
                    rainbow_color = YELLOW_THIRD
                elif y == 5:
                    rainbow_color = GREEN_THIRD
                elif y == 6:
                    rainbow_color = LIGHTBLUE_THIRD
                elif y == 7:
                    rainbow_color = BLUE_THIRD
                else:
                    rainbow_color = PURPLE_THIRD

                curr_colors[x][y] = rainbow_color
    update()

