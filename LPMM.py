import sys
try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("error loading lauchpad.py")

lp = launchpad.LaunchpadMk2();

def get_button_events(lp_object):
    button_events = []
    while True:
        curr_event = lp_object.ButtonStateRaw();
        if curr_event != []:
            button_events.append(curr_event)
        else:
            break
    return button_events

def main():
    if lp.Open(0, "mk2"):
        print("Connected to Launchpad Mk2!")
    else:
        print("Could not connect to Launchpad Mk2, exiting...")
        return
    
    lp.ButtonFlush()
    
    

main()

