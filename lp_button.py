import copy

def get_button_events(lp_object):
    button_events = list()
    while True:
        curr_event = lp_object.ButtonStateXY();
        if curr_event != list():     
            button_events.append(curr_event)
        else:
            break
    return button_events

status = None

def get_button_status(lp_object):
    global status
    
    empty = list()
    for x in range(9):
        empty.append(list())
        for y in range(9):
            if not (x == 0 and y == 8):
                empty[x].append(False)
    
    if status == None:
        status = {k:list() for k in ["state", "changed", "pressed", "released"]}
        status["state"] = copy.deepcopy(empty)
    
    status["changed"] = copy.deepcopy(empty)
    status["pressed"] = copy.deepcopy(empty)
    status["released"] = copy.deepcopy(empty)
    
    button_events = get_button_events(lp_object)
    for event in button_events:
        status["changed"][event[0]][event[1]] = True
        setting = True;
        if event[2] == 0:
            status["released"][event[0]][event[1]] = True
            setting = False
        else:
            status["pressed"][event[0]][event[1]] = True
        status["state"][event[0]][event[1]] = setting



