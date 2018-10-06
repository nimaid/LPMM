import lp_midi, lp_colors

ROOT_COLOR = lp_colors.BLUE
SCALE_COLOR = lp_colors.LIGHT_BLUE
DEFAULT_COLOR = lp_colors.WHITE

SCALE_MAJOR = [0, 2, 4, 5, 7, 9, 11, 12]

scale = SCALE_MAJOR
key = "C"
octave = 1 #0-3
mode = "THIRD"

base_note = None
working_notes = None
working_scale = None
full_working_scale = None

def init():
    global base_note
    global working_notes
    global working_scale
    global full_working_scale
    base_note = lp_midi.name_octave_to_note(key, octave)
    working_scale = [scale[n]+base_note for n in range(len(scale))]

    full_working_scale = []
    for curr_oct in range(4):
        for n in working_scale:
            num = (curr_oct*12)+n
            if len(full_working_scale) > 0:
                if num != full_working_scale[-1]:
                    full_working_scale.append(num)
            else:
                full_working_scale.append(num)
    
    working_notes = [[]]
    for x in range(8):
        working_notes[0].append(None)
    
    for y in range(8, 0, -1):
        working_notes.append([])
        row = 8 - y
        
        offset = None
        if mode == "SEQUENT":
            offset = 8
        elif mode == "THIRD":
            offset = 2
        elif mode == "FOURTH":
            offset = 3

        start_index = (row * offset)
            
        for x in range(8):
            note = full_working_scale[start_index + x]
            working_notes[-1].append(note)
            
        working_notes[-1].append(None)
    working_notes.reverse()

    if mode == "THIRD":
        #Launchpad95 essentiallt swaps X and Y for this...
        working_notes = [list(n) for n in list(zip(*working_notes))]
        working_notes.reverse()
        for n in range(8):
            working_notes[n].reverse()
            working_notes[n] = working_notes[n][1:]+working_notes[n][:1]

def get_keys_bound_to_same_note_as(x, y):
    note = working_notes[y][x]
    same_note = []
    for a in range(8):
        for b in range(8):
            if working_notes[b][a] == note:
                same_note.append((a, b))
    return same_note

def update():
    init()
    
    for y in range(1, 9):
        for x in range(8):
            note = working_notes[y-1][x]
            lp_midi.bind_button_to_note(x, y, note)
            
            if note % 12 == base_note % 12:
                lp_colors.setXY(x, y, ROOT_COLOR)
            elif note % 12 in [n%12 for n in working_scale]:
                lp_colors.setXY(x, y, SCALE_COLOR)
            else:
                lp_colors.setXY(x, y, DEFAULT_COLOR)

def octave_up(x = None, y = None):
    global octave
    if octave < 3:
        octave += 1
    update()

def octave_down(x = None, y = None):
    global octave
    if octave > 0:
        octave -= 1
    update()
