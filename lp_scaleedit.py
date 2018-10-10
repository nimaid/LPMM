import lp_events, lp_colors, lp_instrument

#ERROR when letting go of scaleedit button when holding setting button... note_off gets none note

active = [[False for y in range(9)] for x in range(9)]

def update_active():
    global active
    active = [[False for y in range(9)] for x in range(9)]

    if lp_instrument.mode == "SEQUENT":
        active[3][1] = True
    elif lp_instrument.mode == "THIRD":
        active[4][1] = True
    elif lp_instrument.mode == "FOURTH":
        active[5][1] = True


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

def bind_grid():
    mode_sequent_bindable = lambda x, y : lp_instrument.mode_set("SEQUENT", False)
    lp_events.bind_func_with_colors(3, 1, mode_sequent_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    mode_third_bindable = lambda x, y : lp_instrument.mode_set("THIRD", False)
    lp_events.bind_func_with_colors(4, 1, mode_third_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    mode_fourth_bindable = lambda x, y : lp_instrument.mode_set("FOURTH", False)
    lp_events.bind_func_with_colors(5, 1, mode_fourth_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)

    oct_neg2_bindable = lambda x, y : lp_instrument.octave_set(-2, False)
    lp_events.bind_func_with_colors(0, 4, oct_neg2_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    oct_neg1_bindable = lambda x, y : lp_instrument.octave_set(-1, False)
    lp_events.bind_func_with_colors(1, 4, oct_neg1_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    oct_0_bindable = lambda x, y : lp_instrument.octave_set(0, False)
    lp_events.bind_func_with_colors(2, 4, oct_0_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    oct_1_bindable = lambda x, y : lp_instrument.octave_set(1, False)
    lp_events.bind_func_with_colors(3, 4, oct_1_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
    if lp_instrument.mode != "SEQUENT":
        oct_2_bindable = lambda x, y : lp_instrument.octave_set(2, False)
        lp_events.bind_func_with_colors(4, 4, oct_2_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
        oct_3_bindable = lambda x, y : lp_instrument.octave_set(3, False)
        lp_events.bind_func_with_colors(5, 4, oct_3_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
        oct_4_bindable = lambda x, y : lp_instrument.octave_set(4, False)
        lp_events.bind_func_with_colors(6, 4, oct_4_bindable, lp_colors.RED_THIRD, lp_colors.RED, lp_colors.update_bindable)
        oct_5_bindable = lambda x, y : lp_instrument.octave_set(5, False)
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

def bind_function_keys():
    instrument_mode_bindable = lambda x, y : lp_instrument.set_as_mode()
    lp_events.bind_func_with_colors(8, 1, lp_colors.update_bindable, lp_colors.AMBER_THIRD, lp_colors.AMBER, instrument_mode_bindable)

    oct_up_bindable = lambda x, y : lp_instrument.octave_up(False)
    lp_events.bind_func_with_colors(8, 3, oct_up_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)
    oct_down_bindable = lambda x, y : lp_instrument.octave_down(False)
    lp_events.bind_func_with_colors(8, 4, oct_down_bindable, lp_colors.GREEN_THIRD, lp_colors.GREEN, lp_colors.update_bindable)


def set_as_mode():
    lp_events.mode = "SCALEEDIT"
    lp_events.unbind_all()
    bind_grid()
    bind_function_keys()
    lp_colors.update()
    print("[LPMM] SCALE EDIT MODE")
