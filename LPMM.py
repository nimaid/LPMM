import sys

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("error loading lauchpad.py")

import lp_events, lp_colors


lp = launchpad.LaunchpadMk2();

def hello():
    print("Hello")

def goodbye():
    print("Goodbye")

def main():
    if lp.Open(0, "mk2"):
        print("Connected to Launchpad Mk2!")
    else:
        print("Could not connect to Launchpad Mk2, exiting...")
        return
    
    lp.ButtonFlush()
    
    lp_events.press_funcs[0][1] = hello
    lp_events.release_funcs[0][1] = goodbye
    
    while True:
        lp_events.run(lp)

main()

