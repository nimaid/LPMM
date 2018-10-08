import sys, pygame

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("[launchpad_py] Error loading launchpad.py")

import lp_events, lp_colors, lp_midi, lp_instrument

# print("[LPMM] \n>>> ", end = "")

lp = launchpad.LaunchpadMk2();

def init():
    lp.ButtonFlush()
    lp_events.start(lp)

def main():
    if lp.Open(0, "mk2"):
        print("[LPMM] Connected to Launchpad Mk2!\n>>> ", end = "")
    else:
        print("[LPMM] Could not connect to Launchpad Mk2, exiting...")
        return
    
    init()
    

main()

