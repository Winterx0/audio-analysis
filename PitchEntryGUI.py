'''This is to be the entry window for the program.
It lists the data that is available to be entered by a user
to discover certain properties between light and sound.
'''


import matplotlib.pyplot as plt
from tkinter import *
# from SineWaveGenerator import *


def clicked():

    n = int(pitch_entry.get())

    plt.plot()
    plt.ylabel("Wavelength cm")
    plt.xlabel("Time (Minutes)")
    plt.title("Sine Waveform Generator")
    plt.show()
# ================Pitch Entry=====================


window = Tk()
window.title("Audio Waveform")
window.geometry("720x500")

pitch_button = Button(window, text="Enter", command=clicked, font=("Arial", 50))
pitch_button.grid(column=1, row=0)

pitch_label = Label(window, text="Pick a pitch:  ", font=("Arial", 50))
pitch_label.grid(column=0, row=0)

pitch_entry = Entry(window, font=("Arial", 50))
pitch_entry.grid(column=0, row=1)

octave_label = Label(window, text="The Octave range is from 0 - 8  ", font=("Arial", 20))
octave_label.grid(column=0, row=2)

octave0_label = Label(window, text="Octave 0 entries range from C0 at -48 to B0 at -32", font=("Arial", 20))
octave0_label.grid(column=0, row=3)

octave1_label = Label(window, text="Octave 1 entries range from C1 at -36 to B1 at -25", font=("Arial", 20))
octave1_label.grid(column=0, row=4)

octave2_label = Label(window, text="Octave 2 entries range from C2 at -24 to B2 at -13", font=("Arial", 20))
octave2_label.grid(column=0, row=5)

octave3_label = Label(window, text="Octave 3 entries range from C3 at -12 to B3 at -1", font=("Arial", 20))
octave3_label.grid(column=0, row=6)

octave4_label = Label(window, text="Octave 4 entries range from C4 at 0 to B4 at 11", font=("Arial", 20))
octave4_label.grid(column=0, row=7)

octave5_label = Label(window, text="Octave 5 entries range from C5 at 12 to B5 at 23", font=("Arial", 20))
octave5_label.grid(column=0, row=8)

octave6_label = Label(window, text="Octave 6 entries range from C6 at 24 to B6 at 35", font=("Arial", 20))
octave6_label.grid(column=0, row=9)

octave7_label = Label(window, text="Octave 7 entries range from C7 at 36 to B7 at 47", font=("Arial", 20))
octave7_label.grid(column=0, row=10)

octave8_label = Label(window, text="Octave 8 entries range from C8 at 48 to B8 at 59", font=("Arial", 20))
octave8_label.grid(column=0, row=11)

window.mainloop()

