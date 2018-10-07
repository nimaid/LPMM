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

lp_object = None

def init(lp_object_in):
    global lp_object
    lp_object = lp_object_in
    lp_object.LedAllOn(BLACK)

def setXY(x, y, color):
    curr_colors[x][y] = color
    lp_object.LedCtrlXYByCode(x, y, color)

def effectXY(x, y, color):
    effect_colors[x][y] = color

def getXY(x, y):
    return curr_colors[x][y]

def on_effect(x, y):
    new_color = effect_colors[x][y]
    lp_object.LedCtrlXYByCode(x, y, new_color)

def off_effect(x, y):
    old_color = getXY(x, y)
    lp_object.LedCtrlXYByCode(x, y, old_color)

