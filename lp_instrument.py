import copy, functools
import lp_events, lp_midi, lp_colors, lp_scaleedit

COLOR_ROOT = lp_colors.BLUE
COLOR_SCALE = lp_colors.LIGHTBLUE
COLOR_DEFAULT = lp_colors.WHITE
COLOR_EFFECT = lp_colors.GREEN

SCALE_MAJOR = [0, 2, 4, 5, 7, 9, 11] #VERIFIED
SCALE_MINOR = [0, 2, 3, 5, 7, 8, 10] #VERIFIED
SCALE_DORIAN = [0, 2, 3, 5, 7, 9, 10] #VERIFIED
SCALE_MIXOLYDIAN = [0, 2, 4, 5, 7, 9, 10] #VERIFIED
SCALE_LYDIAN = [0, 2, 4, 6, 7, 9, 11] #VERIFIED
SCALE_PHRYGIAN = [0, 1, 3, 5, 7, 8, 10] #VERIFIED
SCALE_LOCRIAN = [0, 1, 3, 5, 6, 8, 10] #VERIFIED
SCALE_DIMINISHED = [0, 1, 3, 4, 6, 7, 9, 10] #VERIFIED
SCALE_WHOLEHALF = [0, 2, 3, 5, 6, 8, 9, 11] #VERIFIED
SCALE_WHOLETONE = [0, 2, 4, 6, 8, 10] #VERIFIED
SCALE_MINORBLUES = [0, 3, 5, 6, 7, 10] #VERIFIED
SCALE_MINORPENTATONIC = [0, 3, 5, 7, 10] #VERIFIED
SCALE_MAJORPENTATONIC = [0, 2, 4, 7, 9] #VERIFIED
SCALE_HARMONICMINOR = [0, 2, 3, 5, 7, 8, 11] #VERIFIED
SCALE_MELODICMINOR = [0, 2, 3, 5, 7, 9, 11] #VERIFIED
SCALE_SUPERLOCRIAN = [0, 1, 3, 4, 6, 8, 10] #VERIFIED
SCALE_BHIRAV = [0, 1, 4, 5, 7, 8, 11] #VERIFIED
SCALE_HUNGARIANMINOR = [0, 2, 3, 6, 7, 8, 11] #VERIFIED
SCALE_MINORGYPSY = [0, 1, 4, 5, 7, 8, 10] #VERIFIED
SCALE_HIRAJOSHI = [0, 2, 3, 7, 8] #VERIFIED
SCALE_INSEN = [0, 1, 5, 7, 10] #VERIFIED
SCALE_IWATO = [0, 1, 5, 6, 10] #VERIFIED
SCALE_KUMOI = [0, 2, 3, 7, 9] #VERIFIED
SCALE_PELOG = [0, 1, 3, 4, 7, 8] #VERIFIED
SCALE_SPANISH = [0, 1, 3, 4, 5, 6, 8, 10] #VERIFIED
SCALE_IONEOL = [0, 2, 3, 4, 5, 7, 8, 9, 10, 11] #VERIFIED

scale = SCALE_MAJOR #VERIFIED DEFAULT
key = "C" #VERIFIED DEFAULT
octave = 1 #VERIFIED DEFAULT
mode = "FOURTH" #VERIFIED DEFAULT

base_note = None
working_notes = None
working_scale = None
full_working_scale = None



def init():
    global base_note
    global working_notes
    global working_scale
    global full_working_scale
    base_note = lp_midi.name_octave_to_note(key, octave + 1)
    working_scale = [scale[n]+base_note for n in range(len(scale))]

    full_working_scale = []
    for curr_oct in range(12):
        for n in working_scale:
            num = (curr_oct*12)+n
            full_working_scale.append(num)

    working_notes = [[]]
    for x in range(8):
        working_notes[0].append(None)

    for y in range(8, 0, -1):
        working_notes.append([])
        row = 8 - y

        offset = None
        if mode == "THIRD":
            offset = 2
        elif mode == "FOURTH":
            offset = 3

        start_index = None
        if mode == "SEQUENT":
            start_index = len(scale) * row
        else:
            start_index = (row * offset)

        for x in range(8):
            note = full_working_scale[start_index + x]
            working_notes[-1].append(note)

        working_notes[-1].append(None)
    working_notes.reverse()

    if mode == "THIRD":
        #Launchpad95 essentially swaps X and Y for this...
        working_notes = [list(n) for n in list(zip(*working_notes))]
        working_notes.reverse()
        for n in range(8):
            working_notes[n].reverse()
            working_notes[n] = working_notes[n][1:]+working_notes[n][:1]

def get_keys_bound_to_note(note):
    same_note = []
    for a in range(8):
        for b in range(8):
            if working_notes[b][a] == note:
                same_note.append((a, b))
    return same_note

def off_note_and_rebind_new_note(x, y, old_note, new_note):
    lp_midi.note_off(x, y, old_note)
    lp_colors.update()
    lp_midi.bind_button_to_note(x, y, new_note)

def bind_grid():
    init()

    for y in range(1, 9):
        for x in range(8):
            note = working_notes[y-1][x]

            if note % 12 == base_note % 12:
                lp_colors.setXY(x, y, COLOR_ROOT)
            elif note % 12 in [n%12 for n in working_scale]:
                lp_colors.setXY(x, y, COLOR_SCALE)
            else:
                lp_colors.setXY(x, y, COLOR_DEFAULT)

            if lp_events.pressed[x][y]:
                prev_note = lp_midi.note_when_pressed[x][y]
                lp_events.release_funcs[x][y] = functools.partial(off_note_and_rebind_new_note, old_note=prev_note, new_note=note)
            else:
                lp_midi.bind_button_to_note(x, y, note)

def octave_up(rebind=True):
    global octave
    if octave < 5:
        octave += 1
    if mode == "SEQUENT":
        octave = min(octave, 1)
    if(rebind):
        bind_grid()
    lp_colors.update()
    print("[LPMM] OCTAVE UP, NOW " + str(octave) + "\n>>> ", end = "")

def octave_down(rebind=True):
    global octave
    if octave > -2:
        octave -= 1
    if(rebind):
        bind_grid()
    lp_colors.update()
    print("[LPMM] OCTAVE DOWN, NOW " + str(octave) + "\n>>> ", end = "")

def octave_set(oct_in, rebind=True):
    global octave
    octave = min(max(oct_in, -2), 5)
    if mode == "SEQUENT":
        octave = min(octave, 1)
    if rebind:
        bind_grid()
    if lp_events.mode == "SCALEEDIT":
        if octave == -2:
            lp_colors.curr_colors[0][4] == lp_colors.RED
        elif octave == -1:
            lp_colors.curr_colors[1][4] == lp_colors.RED
        elif octave == 0:
            lp_colors.curr_colors[2][4] == lp_colors.RED
        elif octave == 1:
            lp_colors.curr_colors[3][4] == lp_colors.RED
        elif octave == 2:
            lp_colors.curr_colors[4][4] == lp_colors.RED
        elif octave == 3:
            lp_colors.curr_colors[5][4] == lp_colors.RED
        elif octave == 4:
            lp_colors.curr_colors[6][4] == lp_colors.RED
        elif octave == 5:
            lp_colors.curr_colors[7][4] == lp_colors.RED
    lp_colors.update()
    print("[LPMM] OCTAVE DOWN, NOW " + str(octave) + "\n>>> ", end = "")

def key_set(key_in, rebind=True):
    global key
    key = key_in
    if rebind:
        bind_grid()
    lp_colors.update()

def mode_set(mode_in, rebind=True):
    global mode
    global octave
    mode = mode_in
    if mode == "SEQUENT":
        octave = min(octave, 1)
    if rebind:
        bind_grid()
    lp_colors.update()

def scale_set(scale_in, rebind=True):
    global scale
    scale = scale_in
    if rebind:
        bind_grid()
    lp_colors.update()

def bind_function_keys():
    scaleedit_mode_bindable = lambda x, y : lp_scaleedit.set_as_mode()
    lp_events.bind_func_with_colors(8, 1, scaleedit_mode_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)

    oct_up_bindable = lambda x, y : octave_up()
    lp_events.bind_func_with_colors(8, 3, oct_up_bindable, lp_colors.AMBER_THIRD, lp_colors.AMBER, lp_colors.update_bindable)
    oct_down_bindable = lambda x, y : octave_down()
    lp_events.bind_func_with_colors(8, 4, oct_down_bindable, lp_colors.AMBER_THIRD, lp_colors.AMBER, lp_colors.update_bindable)


def set_as_mode():
        lp_events.mode = "INSTRUMENT"
        lp_events.unbind_all()
        bind_grid()
        bind_function_keys()
        lp_colors.update()
