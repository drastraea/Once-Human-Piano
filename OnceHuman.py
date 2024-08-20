"""
Once Human Piano Midi Player

Description: Plays MIDI files by simulating keyboard inputs into game ONCE HUMAN.

Dependencies:
- mido
- pydirectinput
- easygui
- colorama
"""

import mido
import pydirectinput
import time
import argparse
import easygui
from colorama import Fore, Style, init

init()

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, help="Path to midi file to play", dest='path')
parser.add_argument("--pitch", type=int, default=0, help="Pitch modulation to add", dest="pt_mod")
args = parser.parse_args()

def map_piano_note_to_key(note):
    piano_G = ['ctrl', None, 'shift']
    piano_keymap = ['q', '2', 'w', '3', 'e', 'r', '5', 't', '6', 'y', '7', 'u']
    
    # Define note ranges for the three segments
    if 48 <= note <= 59:  # Segment 1: C3 to B3
        change_G = piano_G[0]
        baseline = 48
    elif 60 <= note <= 71:  # Segment 2: C4 to B4
        change_G = piano_G[1]
        baseline = 60
    elif 72 <= note <= 83:  # Segment 3: C5 to B5
        change_G = piano_G[2]
        baseline = 72
    else:
        return '', ''
    
    index = note - baseline
    if 0 <= index < len(piano_keymap):
        return change_G, piano_keymap[index]
    else:
        return '', ''


# Check if the file path is provided as a command-line argument
if args.path:
    midifile = args.path
else:
    midifile = easygui.fileopenbox(title='Select MIDI', filetypes=["*.mid"])
    if midifile is None:
        print(f"{Fore.RED}No MIDI file selected.{Fore.LIGHTGREEN_EX} Please visit https://mayicu.id/{Style.RESET_ALL}")
        quit()

file_name = midifile.rsplit('/', 1)[-1].rsplit('\\', 1)[-1]
print(f"Playing {Fore.GREEN}{file_name}. {Fore.LIGHTGREEN_EX} Please visit https://mayicu.id/{Style.RESET_ALL}")

midi = mido.MidiFile(midifile)
time.sleep(2)
curr_pitch = None
pydirectinput.PAUSE = 0

for msg in midi.play():
    if msg.type == 'note_on' and msg.velocity != 0:
        pitch, key = map_piano_note_to_key(msg.note + args.pt_mod)
        if key:  # Ensure key is not empty
            if curr_pitch != pitch:
                if curr_pitch is not None:
                    pydirectinput.keyUp(curr_pitch)
                if pitch is not None:
                    pydirectinput.keyDown(pitch)
                curr_pitch = pitch
            pydirectinput.press(key)

if curr_pitch is not None:
    pydirectinput.keyUp(curr_pitch)
