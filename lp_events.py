def get_button_events(lp_object):
    button_events = []
    while True:
        curr_event = lp_object.ButtonStateRaw();
        if curr_event != []:     
            button_events.append(curr_event)
        else:
            break
    return button_events


