import lp_midi, lp_colors

ROOT_COLOR = lp_colors.BLUE
SCALE_COLOR = lp_colors.LIGHT_BLUE
DEFAULT_COLOR = lp_colors.WHITE

SCALE_MAJOR = [0, 2, 4, 5, 7, 9, 11, 12]

scale = SCALE_MAJOR
key = "C"
octave = 1 #0-3

base_note = None
working_notes = None

def init():
    global base_note
    global working_notes
    base_note = lp_midi.name_octave_to_note(key, octave)
    
    working_notes = []
    for y in range(1, 9):
        working_notes.append([])
        oct = 7 - y
        for x in range(8):
            note = base_note + (oct * 12) + scale[x]
            working_notes[-1].append(note)

def get_keys_bound_to_same_note_as(x, y):
    note = working_notes[y-1][x]
    same_note = []
    for x in range(8):
        for y in range(1, 9):
            if working_notes[y-1][x] == note:
                same_note.append((x, y))
    return same_note

def update():
    init()
    
    working_scale = [scale[n]+base_note for n in range(len(scale))]
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

