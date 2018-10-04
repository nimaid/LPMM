def HSV_to_RGB(h, s, v):
    h = h % 360 #remove full revolutions
    s = min(max(s, 0), 100) / 100 #limit to 0-1
    v = min(max(v, 0), 100) / 100 #limit to 0-1
    
    c = v * s
    hp = h / 60
    x = c * (1 - abs((hp % 2) - 1))
    
    RGBp = []
    if hp < 1:
        RGBp = [c, x, 0]
    elif hp < 2:
        RGBp = [x, c, 0]
    elif hp < 3:
        RGBp = [0, c, x]
    elif hp < 4:
        RGBp = [0, x, c]
    elif hp < 5:
        RGBp = [x, 0, c]
    elif hp < 6:
        RGBp = [c, 0, x]
    else:
        RGBp = [0, 0, 0]
    
    m = v - c
    RGB = []
    for x in RGBp:
        value = round((x + m) * 255)
        RGB.append(value)
    return RGB

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
