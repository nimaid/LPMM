import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import lp_events, lp_colors, lp_instrument

curr_notes = set()
note_when_pressed = [[None for y in range(9)] for x in range(9)]

pygame.midi.init()

output_ID = pygame.midi.get_default_output_id()
output_info = pygame.midi.get_device_info(output_ID)
player = pygame.midi.Output(output_ID)
print("[LPMM] MIDI Output going to "+str(output_info[0])[2:-1]+": "+str(output_info[1])[2:-1])

def note_on(x, y, note, velocity=127):
    global note_when_pressed
    player.note_on(note, velocity)
    curr_notes.add(note)
    note_when_pressed[x][y] = note
    lp_colors.update()
    print("[LPMM] NOTE " + str(note) + " ON, VELOCITY " + str(velocity))

def note_off(x, y, note):
    global note_when_pressed
    player.note_off(note)
    curr_notes.discard(note)
    note_when_pressed[x][y] = None
    lp_colors.update()
    print("[LPMM] NOTE " + str(note) + " OFF")

def bind_button_to_note(x, y, note, velocity=127):
    lp_events.press_funcs[x][y] = lambda a,b: note_on(a, b, note, velocity)
    lp_events.release_funcs[x][y] = lambda a,b: note_off(a, b, note)


OCT_BASE = 12

NOTE_OFFSETS = {"C":0, "Db":1, "D":2, "Eb":3, "E":4, "F":5, "Gb":6, "G":7, "Ab":8, "A":9, "Bb":10, "B":11}

def name_octave_to_note(name, octave):
    return OCT_BASE + (octave * 12) + NOTE_OFFSETS[name]

def bind_button_to_name_octave(x, y, name, octave, velocity=127):
    note_num = name_octave_to_note(name, octave)
    bind_button_to_note(x, y, note_num, velocity)

