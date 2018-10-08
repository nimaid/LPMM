import copy
import lp_events, lp_midi, lp_colors

ROOT_COLOR = lp_colors.BLUE
SCALE_COLOR = lp_colors.LIGHT_BLUE
DEFAULT_COLOR = lp_colors.WHITE
ACTIVE_COLOR = lp_colors.GREEN

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

old_working_notes = None

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
    lp_midi.note_off(old_note)
    lp_colors.update()
    lp_midi.bind_button_to_note(x, y, new_note)

def update():
    global old_working_notes
    old_working_notes = copy.deepcopy(working_notes)
    
    init()
    
    for y in range(1, 9):
        for x in range(8):
            note = working_notes[y-1][x]
            
            if note % 12 == base_note % 12:
                lp_colors.setXY(x, y, ROOT_COLOR)
            elif note % 12 in [n%12 for n in working_scale]:
                lp_colors.setXY(x, y, SCALE_COLOR)
            else:
                lp_colors.setXY(x, y, DEFAULT_COLOR)

            if lp_events.pressed[x][y]:
                old_note = old_working_notes[y-1][x]
                new_note = note #lambda uses pointers or something so I have to do this
                lp_events.release_funcs[x][y] = lambda a, b : off_note_and_rebind_new_note(a, b, old_note, new_note)
            else:
                lp_midi.bind_button_to_note(x, y, note)

def octave_up():
    global octave
    if octave < 6:
        octave += 1
    if mode == "SEQUENT":
        octave = min(octave, 1)
    update()
    lp_colors.update()

def octave_down():
    global octave
    if octave > -2:
        octave -= 1
    update()
    lp_colors.update()

def octave_set(oct_in):
    global octave
    octave = min(max(oct_in, -2), 6)
    if mode == "SEQUENT":
        octave = min(octave, 1)
    update()
    lp_colors.update()

def key_set(key_in):
    global key
    key = key_in
    update()
    lp_colors.update()

def mode_set(mode_in):
    global mode
    global octave
    mode = mode_in
    if mode == "SEQUENT":
        octave = min(octave, 1)
    update()
    lp_colors.update()

def scale_set(scale_in):
    global scale
    scale = scale_in
    update()
    lp_colors.update()

def bind_function_keys():
    oct_up_bindable = lambda x, y : octave_up()
    colors_update_bindable = lambda x, y : lp_colors.update()
    lp_events.bind_func_with_colors(8, 3, oct_up_bindable, lp_colors.AMBER_THIRD, lp_colors.AMBER, colors_update_bindable)
    oct_down_bindable = lambda x, y : octave_down()
    lp_events.bind_func_with_colors(8, 4, oct_down_bindable, lp_colors.AMBER_THIRD, lp_colors.AMBER, colors_update_bindable)
