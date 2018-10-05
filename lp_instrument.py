import lp_midi, lp_colors

ROOT_COLOR = lp_colors.BLUE
SCALE_COLOR = lp_colors.LIGHT_BLUE
DEFAULT_COLOR = lp_colors.WHITE

SCALE_MAJOR = [0, 2, 4, 5, 7, 9, 11, 12]

SCALE = SCALE_MAJOR

key = "A"
octave = 1

base_note = lp_midi.name_octave_to_note(key, octave)
actual_scale = [(SCALE[n]+base_note) for n in range(len(SCALE))]

def update():
    for y in range(8, 0, -1):
        for x in range(8):
            oct = (7 - y)
            note = base_note + (oct * 12) + SCALE[x]
            lp_midi.bind_button_to_note(x, y, note)
            
            if note % 12 == base_note % 12:
                lp_colors.setXY(x, y, ROOT_COLOR)
            elif note % 12 in [n%12 for n in actual_scale]:
                lp_colors.setXY(x, y, SCALE_COLOR)
            else:
                lp_colors.setXY(x, y, DEFAULT_COLOR)
