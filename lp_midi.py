import pygame
import lp_events

pygame.midi.init()

def note_on(note, velocity=127):
    player.note_on(note, velocity)

output_ID = pygame.midi.get_default_output_id()
output_info = pygame.midi.get_device_info(output_ID)
player = pygame.midi.Output(output_ID)
print("MIDI Output going to "+str(output_info[0])[2:-1]+" : "+str(output_info[1])[2:-1])

def note_on(note, velocity=127):
    player.note_on(note, velocity)

def note_off(note):
    player.note_off(note)

def bind_button_to_note(x, y, note, velocity=127):
    lp_events.press_funcs[x][y] = lambda a,b: note_on(note, velocity)
    lp_events.release_funcs[x][y] = lambda a,b: note_off(note)

OCT_BASE = [12, 24, 36, 48, 60, 72, 84, 96, 108]

NOTE_OFFSETS = {"C":0, "Cs":1, "D":2, "Ds":3, "E":4, "F":5, "Fs":6, "G":7, "Gs":8, "A":9, "As":10, "B":11}

def name_octave_to_note(name, octave):
    return OCT_BASE[octave] + NOTE_OFFSETS[name]

def bind_button_to_name_octave(x, y, name, octave, velocity=127):
    note_num = name_octave_to_note(name, octave)
    bind_button_to_note(x, y, note_num, velocity)


