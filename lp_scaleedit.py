import functools
import lp_events, lp_colors, lp_instrument, lp_midi

active = [[False for y in range(9)] for x in range(9)]
is_active = False

def update_active():
    global active
    active = [[False for y in range(9)] for x in range(9)]

    if lp_instrument.mode == "CHROMATICGUITAR":
        active[2][1] = True
    elif lp_instrument.mode == "SEQUENT":
        active[3][1] = True
    elif lp_instrument.mode == "THIRD":
        active[4][1] = True
    elif lp_instrument.mode == "FOURTH":
        active[5][1] = True
    elif lp_instrument.mode == "CHROMATIC":
        active[6][1] = True

    if lp_instrument.key == "C":
        active[0][3] = True
    elif lp_instrument.key == "Db":
        active[0][2] = True
    elif lp_instrument.key == "D":
        active[1][3] = True
    elif lp_instrument.key == "Eb":
        active[1][2] = True
    elif lp_instrument.key == "E":
        active[2][3] = True
    elif lp_instrument.key == "F":
        active[3][3] = True
    elif lp_instrument.key == "Gb":
        active[3][2] = True
    elif lp_instrument.key == "G":
        active[4][3] = True
    elif lp_instrument.key == "Ab":
        active[4][2] = True
    elif lp_instrument.key == "A":
        active[5][3] = True
    elif lp_instrument.key == "Bb":
        active[5][2] = True
    elif lp_instrument.key == "B":
        active[6][3] = True

    if lp_instrument.octave == -2:
        active[0][4] = True
    elif lp_instrument.octave == -1:
        active[1][4] = True
    elif lp_instrument.octave == 0:
        active[2][4] = True
    elif lp_instrument.octave == 1:
        active[3][4] = True
    elif lp_instrument.octave == 2:
        active[4][4] = True
    elif lp_instrument.octave == 3:
        active[5][4] = True
    elif lp_instrument.octave == 4:
        active[6][4] = True
    elif lp_instrument.octave == 5:
        active[7][4] = True

    if lp_instrument.scale == lp_instrument.SCALE_MAJOR:
        active[0][5] = True
    elif lp_instrument.scale == lp_instrument.SCALE_MINOR:
        active[1][5] = True
    elif lp_instrument.scale == lp_instrument.SCALE_DORIAN:
        active[2][5] = True
    elif lp_instrument.scale == lp_instrument.SCALE_MIXOLYDIAN:
        active[3][5] = True
    elif lp_instrument.scale == lp_instrument.SCALE_LYDIAN:
        active[4][5] = True
    elif lp_instrument.scale == lp_instrument.SCALE_PHRYGIAN:
        active[5][5] = True
    elif lp_instrument.scale == lp_instrument.SCALE_LOCRIAN:
        active[6][5] = True
    elif lp_instrument.scale == lp_instrument.SCALE_DIMINISHED:
        active[7][5] = True
    elif lp_instrument.scale == lp_instrument.SCALE_WHOLEHALF:
        active[0][6] = True
    elif lp_instrument.scale == lp_instrument.SCALE_WHOLETONE:
        active[1][6] = True
    elif lp_instrument.scale == lp_instrument.SCALE_MINORBLUES:
        active[2][6] = True
    elif lp_instrument.scale == lp_instrument.SCALE_MINORPENTATONIC:
        active[3][6] = True
    elif lp_instrument.scale == lp_instrument.SCALE_MAJORPENTATONIC:
        active[4][6] = True
    elif lp_instrument.scale == lp_instrument.SCALE_HARMONICMINOR:
        active[5][6] = True
    elif lp_instrument.scale == lp_instrument.SCALE_MELODICMINOR:
        active[6][6] = True
    elif lp_instrument.scale == lp_instrument.SCALE_SUPERLOCRIAN:
        active[7][6] = True
    elif lp_instrument.scale == lp_instrument.SCALE_BHAIRAV:
        active[0][7] = True
    elif lp_instrument.scale == lp_instrument.SCALE_HUNGARIANMINOR:
        active[1][7] = True
    elif lp_instrument.scale == lp_instrument.SCALE_MINORGYPSY:
        active[2][7] = True
    elif lp_instrument.scale == lp_instrument.SCALE_HIRAJOSHI:
        active[3][7] = True
    elif lp_instrument.scale == lp_instrument.SCALE_INSEN:
        active[4][7] = True
    elif lp_instrument.scale == lp_instrument.SCALE_IWATO:
        active[5][7] = True
    elif lp_instrument.scale == lp_instrument.SCALE_KUMOI:
        active[6][7] = True
    elif lp_instrument.scale == lp_instrument.SCALE_PELOG:
        active[7][7] = True
    elif lp_instrument.scale == lp_instrument.SCALE_SPANISH:
        active[0][8] = True
    elif lp_instrument.scale == lp_instrument.SCALE_IONEOL:
        active[1][8] = True

def note_off_and_bind_old_release_func(x, y, old_func, note):
    lp_midi.note_off(x, y, note)
    lp_events.release_funcs[x][y] = old_func

def rebind_pressed_notes():
    for x in range(8):
        for y in range(1, 9):
            if lp_events.pressed[x][y] and (lp_midi.note_when_pressed[x][y] in lp_midi.curr_notes):
                old_note = lp_midi.note_when_pressed[x][y]
                old_func_in = lp_events.release_funcs[x][y]

                lp_events.release_funcs[x][y] = functools.partial(note_off_and_bind_old_release_func, old_func=old_func_in, note=old_note)

def bind_grid():
    mode_chromaticguitar_bindable = lambda x, y : lp_instrument.mode_set("CHROMATICGUITAR", False)
    lp_events.bind_func_with_colors(2, 1, mode_chromaticguitar_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    mode_sequent_bindable = lambda x, y : lp_instrument.mode_set("SEQUENT", False)
    lp_events.bind_func_with_colors(3, 1, mode_sequent_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    mode_third_bindable = lambda x, y : lp_instrument.mode_set("THIRD", False)
    lp_events.bind_func_with_colors(4, 1, mode_third_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    mode_fourth_bindable = lambda x, y : lp_instrument.mode_set("FOURTH", False)
    lp_events.bind_func_with_colors(5, 1, mode_fourth_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    mode_chromatic_bindable = lambda x, y : lp_instrument.mode_set("CHROMATIC", False)
    lp_events.bind_func_with_colors(6, 1, mode_chromatic_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)

    key_C_bindable = lambda x, y : lp_instrument.key_set("C", False)
    lp_events.bind_func_with_colors(0, 3, key_C_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)
    key_Db_bindable = lambda x, y : lp_instrument.key_set("Db", False)
    lp_events.bind_func_with_colors(0, 2, key_Db_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)
    key_D_bindable = lambda x, y : lp_instrument.key_set("D", False)
    lp_events.bind_func_with_colors(1, 3, key_D_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)
    key_Eb_bindable = lambda x, y : lp_instrument.key_set("Eb", False)
    lp_events.bind_func_with_colors(1, 2, key_Eb_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)
    key_E_bindable = lambda x, y : lp_instrument.key_set("E", False)
    lp_events.bind_func_with_colors(2, 3, key_E_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)
    key_F_bindable = lambda x, y : lp_instrument.key_set("F", False)
    lp_events.bind_func_with_colors(3, 3, key_F_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)
    key_Gb_bindable = lambda x, y : lp_instrument.key_set("Gb", False)
    lp_events.bind_func_with_colors(3, 2, key_Gb_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)
    key_G_bindable = lambda x, y : lp_instrument.key_set("G", False)
    lp_events.bind_func_with_colors(4, 3, key_G_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)
    key_Ab_bindable = lambda x, y : lp_instrument.key_set("Ab", False)
    lp_events.bind_func_with_colors(4, 2, key_Ab_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)
    key_A_bindable = lambda x, y : lp_instrument.key_set("A", False)
    lp_events.bind_func_with_colors(5, 3, key_A_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)
    key_Bb_bindable = lambda x, y : lp_instrument.key_set("Bb", False)
    lp_events.bind_func_with_colors(5, 2, key_Bb_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)
    key_B_bindable = lambda x, y : lp_instrument.key_set("B", False)
    lp_events.bind_func_with_colors(6, 3, key_B_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)

    oct_neg2_bindable = lambda x, y : lp_instrument.octave_set(-2, False)
    if lp_instrument.octave_is_valid(-2):
        lp_events.bind_func_with_colors(0, 4, oct_neg2_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    oct_neg1_bindable = lambda x, y : lp_instrument.octave_set(-1, False)
    if lp_instrument.octave_is_valid(-1):
        lp_events.bind_func_with_colors(1, 4, oct_neg1_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    oct_0_bindable = lambda x, y : lp_instrument.octave_set(0, False)
    if lp_instrument.octave_is_valid(0):
        lp_events.bind_func_with_colors(2, 4, oct_0_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    oct_1_bindable = lambda x, y : lp_instrument.octave_set(1, False)
    if lp_instrument.octave_is_valid(1):
        lp_events.bind_func_with_colors(3, 4, oct_1_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    oct_2_bindable = lambda x, y : lp_instrument.octave_set(2, False)
    if lp_instrument.octave_is_valid(2):
        lp_events.bind_func_with_colors(4, 4, oct_2_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    oct_3_bindable = lambda x, y : lp_instrument.octave_set(3, False)
    if lp_instrument.octave_is_valid(3):
        lp_events.bind_func_with_colors(5, 4, oct_3_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    oct_4_bindable = lambda x, y : lp_instrument.octave_set(4, False)
    if lp_instrument.octave_is_valid(4):
        lp_events.bind_func_with_colors(6, 4, oct_4_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    oct_5_bindable = lambda x, y : lp_instrument.octave_set(5, False)
    if lp_instrument.octave_is_valid(5):
        lp_events.bind_func_with_colors(7, 4, oct_5_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)

    scale_major_bindable = lambda x, y : lp_instrument.scale_set("MAJOR", False)
    lp_events.bind_func_with_colors(0, 5, scale_major_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_minor_bindable = lambda x, y : lp_instrument.scale_set("MINOR", False)
    lp_events.bind_func_with_colors(1, 5, scale_minor_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_dorian_bindable = lambda x, y : lp_instrument.scale_set("DORIAN", False)
    lp_events.bind_func_with_colors(2, 5, scale_dorian_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_mixolydian_bindable = lambda x, y : lp_instrument.scale_set("MIXOLYDIAN", False)
    lp_events.bind_func_with_colors(3, 5, scale_mixolydian_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_lydian_bindable = lambda x, y : lp_instrument.scale_set("LYDIAN", False)
    lp_events.bind_func_with_colors(4, 5, scale_lydian_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_phrygian_bindable = lambda x, y : lp_instrument.scale_set("PHRYGIAN", False)
    lp_events.bind_func_with_colors(5, 5, scale_phrygian_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_locrian_bindable = lambda x, y : lp_instrument.scale_set("LOCRIAN", False)
    lp_events.bind_func_with_colors(6, 5, scale_locrian_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_diminished_bindable = lambda x, y : lp_instrument.scale_set("DIMINISHED", False)
    lp_events.bind_func_with_colors(7, 5, scale_diminished_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_wholehalf_bindable = lambda x, y : lp_instrument.scale_set("WHOLEHALF", False)
    lp_events.bind_func_with_colors(0, 6, scale_wholehalf_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_wholetone_bindable = lambda x, y : lp_instrument.scale_set("WHOLETONE", False)
    lp_events.bind_func_with_colors(1, 6, scale_wholetone_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_minorblues_bindable = lambda x, y : lp_instrument.scale_set("MINORBLUES", False)
    lp_events.bind_func_with_colors(2, 6, scale_minorblues_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_minorpentatonic_bindable = lambda x, y : lp_instrument.scale_set("MINORPENTATONIC", False)
    lp_events.bind_func_with_colors(3, 6, scale_minorpentatonic_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_majorpentatonic_bindable = lambda x, y : lp_instrument.scale_set("MAJORPENTATONIC", False)
    lp_events.bind_func_with_colors(4, 6, scale_majorpentatonic_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_harmonicminor_bindable = lambda x, y : lp_instrument.scale_set("HARMONICMINOR", False)
    lp_events.bind_func_with_colors(5, 6, scale_harmonicminor_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_melodicminor_bindable = lambda x, y : lp_instrument.scale_set("MELODICMINOR", False)
    lp_events.bind_func_with_colors(6, 6, scale_melodicminor_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_superlocrian_bindable = lambda x, y : lp_instrument.scale_set("SUPERLOCRIAN", False)
    lp_events.bind_func_with_colors(7, 6, scale_superlocrian_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_bhairav_bindable = lambda x, y : lp_instrument.scale_set("BHAIRAV", False)
    lp_events.bind_func_with_colors(0, 7, scale_bhairav_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_hungarianminor_bindable = lambda x, y : lp_instrument.scale_set("HUNGARIANMINOR", False)
    lp_events.bind_func_with_colors(1, 7, scale_hungarianminor_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_minorgypsy_bindable = lambda x, y : lp_instrument.scale_set("MINORGYPSY", False)
    lp_events.bind_func_with_colors(2, 7, scale_minorgypsy_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_hirajoshi_bindable = lambda x, y : lp_instrument.scale_set("HIRAJOSHI", False)
    lp_events.bind_func_with_colors(3, 7, scale_hirajoshi_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_insen_bindable = lambda x, y : lp_instrument.scale_set("INSEN", False)
    lp_events.bind_func_with_colors(4, 7, scale_insen_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_iwato_bindable = lambda x, y : lp_instrument.scale_set("IWATO", False)
    lp_events.bind_func_with_colors(5, 7, scale_iwato_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_kumoi_bindable = lambda x, y : lp_instrument.scale_set("KUMOI", False)
    lp_events.bind_func_with_colors(6, 7, scale_kumoi_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_pelog_bindable = lambda x, y : lp_instrument.scale_set("PELOG", False)
    lp_events.bind_func_with_colors(7, 7, scale_pelog_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_spanish_bindable = lambda x, y : lp_instrument.scale_set("SPANISH", False)
    lp_events.bind_func_with_colors(0, 8, scale_spanish_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)
    scale_ioneol_bindable = lambda x, y : lp_instrument.scale_set("IONEOL", False)
    lp_events.bind_func_with_colors(1, 8, scale_ioneol_bindable, lp_colors.BLUE_THIRD, lp_colors.BLUE, lp_colors.update_bindable)

    rebind_pressed_notes()

def bind_function_keys():
    instrument_mode_bindable = lambda x, y : lp_instrument.set_as_mode()
    lp_events.bind_func_with_colors(8, 1, lp_colors.update_bindable, lp_colors.AMBER_THIRD, lp_colors.AMBER, instrument_mode_bindable)

    oct_up_bindable = lambda x, y : lp_instrument.octave_up(False)
    lp_events.bind_func_with_colors(8, 3, oct_up_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)
    oct_down_bindable = lambda x, y : lp_instrument.octave_down(False)
    lp_events.bind_func_with_colors(8, 4, oct_down_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)


def set_as_mode():
    global is_active
    lp_events.mode = "SCALEEDIT"
    lp_events.unbind_all()
    bind_grid()
    bind_function_keys()
    lp_colors.update()
    is_active = True
    lp_instrument.is_active = False
    print("[LPMM] SCALE EDIT MODE")
