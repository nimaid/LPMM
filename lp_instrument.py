import lp_midi, lp_colors

ROOT_COLOR = lp_colors.BLUE
SCALE_COLOR = lp_colors.LIGHT_BLUE
DEFAULT_COLOR = lp_colors.WHITE

SCALE_MAJOR = [0, 2, 4, 5, 7, 9, 11, 12]

scale = SCALE_MAJOR
key = "C"
octave = 1 #0-3
mode = "THIRD" #

base_note = None
working_notes = None
working_scale = None

def init():
    global base_note
    global working_notes
    global working_scale
    base_note = lp_midi.name_octave_to_note(key, octave)
    working_scale = [scale[n]+base_note for n in range(len(scale))]
    
    working_notes = [[]]
    for x in range(8):
        working_notes[0].append(None)
    
    for y in range(8, 0, -1):
        working_notes.append([])
        row = 8 - y
        print("Row " + str(row))
        row_offset = 0
        for x in range(8):
            offset = None
            if mode == "SEQUENT":
                offset = 8
            elif mode == "THIRD":
                offset = 2
            
            scale_add = x + (row * offset)
            print("  scale_add: " + str(scale_add))
            if scale_add in range(8):
                note = base_note + working_scale[scale_add]
                working_notes[-1].append(note)
                print("    Note: " + str(note))
            elif scale_add > 7:
                note = base_note
                scale_add_offset = scale_add + row_offset
                while (scale_add_offset // 8) > 0:
                    print("    Remapping down: " + str(scale_add_offset), end="")
                    note += 12
                    scale_add_offset -= 8
                    
                    print(" -> " + str(scale_add_offset))
                note += working_scale[scale_add_offset]
                if len(working_notes[-1]) > 0:
                    if note == working_notes[-1][-1]:
                        print("    Nudging up: " + str(scale_add_offset), end="")
                        row_offset += 1
                        scale_add_offset += 1
                        scale_add_offset %= 8
                        print(" -> " + str(scale_add_offset))
                        print("      row_offset: " + str(row_offset))
                        note -= 24
                        note += working_scale[scale_add_offset]
                if (x == 0) and (len(working_notes[-2]) > 0):
                    if False:
                        print("    Nudging up: " + str(scale_add_offset), end="")
                        row_offset += 1
                        scale_add_offset += 1
                        scale_add_offset %= 8
                        print(" -> " + str(scale_add_offset))
                        print("      row_offset: " + str(row_offset))
                        note -= 24
                        note += working_scale[scale_add_offset]
                working_notes[-1].append(note)
                print("    Note: " + str(note))
            else:
                None
            
        working_notes[-1].append(None)
    working_notes.reverse()

def get_keys_bound_to_same_note_as(x, y):
    note = working_notes[y][x]
    same_note = []
    for x in range(8):
        for y in range(8):
            if working_notes[y][x] == note:
                same_note.append((x, y))
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
