import lp_events, lp_colors, lp_instrument

def bind_grid():
    lp_events.unbind_all()

    colors_update_bindable = lambda x, y : lp_colors.update()

    oct_neg2_bindable = lambda x, y : lp_instrument.octave_set(-2)
    lp_events.bind_func_with_colors(0, 4, oct_neg2_bindable, lp_colors.RED_THIRD, lp_colors.RED, colors_update_bindable)

    oct_neg1_bindable = lambda x, y : lp_instrument.octave_set(-1)
    lp_events.bind_func_with_colors(1, 4, oct_neg1_bindable, lp_colors.RED_THIRD, lp_colors.RED)

    oct_0_bindable = lambda x, y : lp_instrument.octave_set(0)
    lp_events.bind_func_with_colors(2, 4, oct_0_bindable, lp_colors.RED_THIRD, lp_colors.RED)
