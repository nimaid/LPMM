import sys, pygame

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("error loading lauchpad.py")

import lp_events, lp_colors, lp_midi


lp = launchpad.LaunchpadMk2();

def init():
    lp.ButtonFlush()
    lp_events.start(lp)

def main():
    if lp.Open(0, "mk2"):
        print("Connected to Launchpad Mk2!")
    else:
        print("Could not connect to Launchpad Mk2, exiting...")
        return
    
    init()
    

main()

