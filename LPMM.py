import sys
try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("error loading lauchpad.py")
import lp_events

lp = launchpad.LaunchpadMk2();

def main():
    if lp.Open(0, "mk2"):
        print("Connected to Launchpad Mk2!")
    else:
        print("Could not connect to Launchpad Mk2, exiting...")
        return
    
    lp.ButtonFlush()
    
    

main()

