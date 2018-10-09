import lp_events, lp_colors, lp_instrument

active = [[False for y in range(9)] for x in range(9)]

def update_active():
    global active
    active = [[False for y in range(9)] for x in range(9)]

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

def bind_grid():
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

def bind_function_keys():
    instrument_mode_bindable = lambda x, y : lp_instrument.set_as_mode()
    lp_events.bind_func_with_colors(8, 1, lp_colors.update_bindable, lp_colors.RED_THIRD, lp_colors.RED, instrument_mode_bindable)

    oct_up_bindable = lambda x, y : lp_instrument.octave_up(False)
    lp_events.bind_func_with_colors(8, 3, oct_up_bindable, lp_colors.AMBER_THIRD, lp_colors.AMBER, lp_colors.update_bindable)
    oct_down_bindable = lambda x, y : lp_instrument.octave_down(False)
    lp_events.bind_func_with_colors(8, 4, oct_down_bindable, lp_colors.AMBER_THIRD, lp_colors.AMBER, lp_colors.update_bindable)


def set_as_mode():
    lp_events.mode = "SCALEEDIT"
    lp_events.unbind_all()
    bind_grid()
    bind_function_keys()
    lp_colors.update()
    print("[LPMM] SCALE EDIT MODE")
