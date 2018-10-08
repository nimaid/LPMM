note_when_presed = [[None for y in range(9)] for x in range(9)]

def note_on(x, y, note, velocity=127):
    global note_when_pressed
    note_when_pressed[x][y] = note

def note_off(x, y, note):
    global note_when_pressed
    note_when_pressed[x][y] = None
