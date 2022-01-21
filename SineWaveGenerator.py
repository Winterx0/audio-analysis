'''This is the initial sine waveform generator. At this time it is programed to
only play a sound until I am able to add changable elements to construct a
specific pitch to be displayed in Matplotlib and converted via Wavelength to the
visible color spectrum as well as to BPM that can be used to identify input
from an external device later'''

''' Listed below are the Octaves You would see on a piano,
 based on the notation data provided. To discover the different 
 pitch properties listed, you can un-highlight one of the 
 sinewave.set_pitch() parameters to hear the tonal property'''

import time
from pysinewave import SineWave
# from PitchEntryGUI import *


# class SoundWaveGenerator:
# def generator():

sinewave = SineWave(pitch=12, pitch_per_second=10)

print("Sinewave Starts")

# ==============Octave 0=================

# sinewave.set_pitch(-37)  # Note B0, Frequency 30.87, Wavelength 1117.67cm
# sinewave.set_pitch(-38)  # Note A#/Bb0, Frequency 29.14, Wavelength 1184.13cm
# sinewave.set_pitch(-39)  # Note A0, Frequency 27.50, Wavelength 1254.55cm
# sinewave.set_pitch(-40)  # Note G#/Ab0, Frequency 25.96, Wavelength 1329.14cm
# sinewave.set_pitch(-41)  # Note G0, Frequency 24.50, Wavelength 1408.18cm
# sinewave.set_pitch(-42)  # Note F#/Gb0, Frequency 23.12, Wavelength 1491.91cm
# sinewave.set_pitch(-43)  # Note F0, Frequency 21.83, Wavelength 1580.63cm
# sinewave.set_pitch(-44)  # Note E0, Frequency 20.60, Wavelength 1674.62cm
# sinewave.set_pitch(-45)  # Note D#/Eb0, Frequency 19.45, Wavelength 1774.20cm
# sinewave.set_pitch(-46)  # Note D0, Frequency 18.35, Wavelength 1879.69cm
# sinewave.set_pitch(-47)  # Note C#/Db0, Frequency 17.32, Wavelength 1991.47cm
# sinewave.set_pitch(-48)  # Note C0, Frequency 16.35, Wavelength 2109.89cm

# ==============Octave 1=================

# sinewave.set_pitch(-25)  # Note B1, Frequency 61.74, Wavelength 558.84cm
# sinewave.set_pitch(-26)  # Note A#/Bb1, Frequency 58.27, Wavelength 592.07cm
# sinewave.set_pitch(-27)  # Note A1, Frequency 55.00, Wavelength 627.27cm
# sinewave.set_pitch(-28)  # Note G#/Ab1, Frequency 51.91, Wavelength 664.57cm
# sinewave.set_pitch(-29)  # Note G1, Frequency 49.00, Wavelength 704.09cm
# sinewave.set_pitch(-30)  # Note F#/Gb1, Frequency 46.25, Wavelength 745.96cm
# sinewave.set_pitch(-31)  # Note F1, Frequency 43.65, Wavelength 790.31cm
# sinewave.set_pitch(-32)  # Note E1, Frequency 41.20, Wavelength 837.31cm
# sinewave.set_pitch(-33)  # Note D#/Eb1, Frequency 38.89, Wavelength 887.10cm
# sinewave.set_pitch(-34)  # Note D1, Frequency 36.71, Wavelength 939.85cm
# sinewave.set_pitch(-35)  # Note C#/Db1, Frequency 34.65, Wavelength 995.73cm
# sinewave.set_pitch(-36)  # Note C1, Frequency 32.70, Wavelength 1054.94cm

# ==============Octave 2=================

# sinewave.set_pitch(-13)  # Note B2, Frequency 123.47, Wavelength 279.42cm
# sinewave.set_pitch(-14)  # Note A#/Bb2, Frequency 116.54, Wavelength 296.03cm
# sinewave.set_pitch(-15)  # Note A2, Frequency 110.00, Wavelength 313.64cm
# sinewave.set_pitch(-16)  # Note G#/Ab2, Frequency 103.83, Wavelength 332.29cm
# sinewave.set_pitch(-17)  # Note G2, Frequency 98.00, Wavelength 352.04cm
# sinewave.set_pitch(-18)  # Note F#/Gb2, Frequency 92.50, Wavelength 372.98cm
# sinewave.set_pitch(-19)  # Note F2, Frequency 87.31, Wavelength 395.16cm
# sinewave.set_pitch(-20)  # Note E2, Frequency 82.41, Wavelength 418.65cm
# sinewave.set_pitch(-21)  # Note D#/Eb2, Frequency 77.78, Wavelength 443.55cm
# sinewave.set_pitch(-22)  # Note D2, Frequency 73.42, Wavelength 469.92cm
# sinewave.set_pitch(-23)  # Note C#/Db2, Frequency 69.30, Wavelength 497.87cm
# sinewave.set_pitch(-24)  # Note C2, Frequency 65.41, Wavelength 527.47cm

# ==============Octave 3=================

# sinewave.set_pitch(-1)  # Note B3, Frequency 246.94, Wavelength 139.71cm
# sinewave.set_pitch(-2)  # Note A#/Bb3, Frequency 233.08, Wavelength 148.02cm
# sinewave.set_pitch(-3)  # Note A3, Frequency 220.00, Wavelength 156.82cm
# sinewave.set_pitch(-4)  # Note G#/Ab3, Frequency 207.65, Wavelength 166.14cm
# sinewave.set_pitch(-5)  # Note G3, Frequency 196.00, Wavelength 176.02cm
# sinewave.set_pitch(-6)  # Note F#/Gb3, Frequency 185.00, Wavelength 186.49cm
# sinewave.set_pitch(-7)  # Note F3, Frequency 174.61, Wavelength 197.58cm
# sinewave.set_pitch(-8)  # Note E3, Frequency 164.81, Wavelength 209.33cm
# sinewave.set_pitch(-9)  # Note D#/Eb3, Frequency 155.56, Wavelength 221.77cm
# sinewave.set_pitch(-10)  # Note D3, Frequency 146.83, Wavelength 234.96cm
# sinewave.set_pitch(-11)  # Note C#/Db3, Frequency 138.59, Wavelength 248.93cm
sinewave.set_pitch(-12)  # Note C3, Frequency 130.81, Wavelength 263.74cm

# ==============Octave 4=================

# sinewave.set_pitch(0)  # Note C4, Frequency 261.63, Wavelength 131.87cm
# sinewave.set_pitch(1)  # Note C#/Db4, Frequency 277.18, Wavelength 124.47cm
# sinewave.set_pitch(2)  # Note D4, Frequency 293.66, Wavelength 117.48cm
# sinewave.set_pitch(3)  # Note D#/Eb4, Frequency 311.13, Wavelength 110.89cm
# sinewave.set_pitch(4)  # Note E4, Frequency 329.63, Wavelength 104.66cm
# sinewave.set_pitch(5)  # Note F4, Frequency 349.23, Wavelength 98.79cm
# sinewave.set_pitch(6)  # Note F#/Gb4, Frequency 369.99, Wavelength 93.24cm
# sinewave.set_pitch(7)  # Note G4, Frequency 392.00, Wavelength 88.01cm
# sinewave.set_pitch(8)  # Note G#/Ab4, Frequency 415.30, Wavelength 83.07cm
# sinewave.set_pitch(9)  # Note A4, Frequency 440.00, Wavelength 78.41cm
# sinewave.set_pitch(10)  # Note A#/Bb4, Frequency 466.16, Wavelength 74.01cm
# sinewave.set_pitch(11)  # Note B4, Frequency 493.88, Wavelength 69.85cm

# ==============Octave 5=================

# sinewave.set_pitch(12)  # Note C5, Frequency 523.25, Wavelength 65.93cm
# sinewave.set_pitch(13)  # Note C#/Db5, Frequency 554.37, Wavelength 62.23cm
# sinewave.set_pitch(14)  # Note D5, Frequency 587.33, Wavelength 58.74cm
# sinewave.set_pitch(15)  # Note D#/Eb5, Frequency 622.25, Wavelength 55.44cm
# sinewave.set_pitch(16)  # Note E5, Frequency 659.25, Wavelength 52.33cm
# sinewave.set_pitch(17)  # Note F5, Frequency 698.46, Wavelength 49.39cm
# sinewave.set_pitch(18)  # Note F#/Gb5, Frequency 739.99, Wavelength 46.62cm
# sinewave.set_pitch(19)  # Note G5, Frequency 783.99, Wavelength 44.01cm
# sinewave.set_pitch(20)  # Note G#/Ab5, Frequency 830.61, Wavelength 41.54cm
# sinewave.set_pitch(21)  # Note A5, Frequency 880.00, Wavelength 39.20cm
# sinewave.set_pitch(22)  # Note A#/Bb5, Frequency 932.33, Wavelength 37.00cm
# sinewave.set_pitch(23)  # Note B5, Frequency 987.77, Wavelength 34.93cm

# ==============Octave 6=================

# sinewave.set_pitch(24)  # Note C6, Frequency 1046.50, Wavelength 32.97cm
# sinewave.set_pitch(25)  # Note C#/Db6, Frequency 1108.73, Wavelength 31.12cm
# sinewave.set_pitch(26)  # Note D6, Frequency 1174.66, Wavelength 29.37cm
# sinewave.set_pitch(27)  # Note D#/Eb6, Frequency 1244.51, Wavelength 27.72cm
# sinewave.set_pitch(28)  # Note E6, Frequency 1318.51, Wavelength 26.17cm
# sinewave.set_pitch(29)  # Note F6, Frequency 1396.91, Wavelength 24.70cm
# sinewave.set_pitch(30)  # Note F#/Gb6, Frequency 1479.98, Wavelength 23.31cm
# sinewave.set_pitch(31)  # Note G6, Frequency 1567.98, Wavelength 22.00cm
# sinewave.set_pitch(32)  # Note G#/Ab6, Frequency 1661.22, Wavelength 20.77cm
# sinewave.set_pitch(33)  # Note A6, Frequency 1760.00, Wavelength 19.60cm
# sinewave.set_pitch(34)  # Note A#/Bb6, Frequency 1864.66, Wavelength 18.50cm
# sinewave.set_pitch(35)  # Note B6, Frequency 1975.53, Wavelength 17.46cm

# ==============Octave 7=================

# sinewave.set_pitch(36)  # Note C7, Frequency 2093.00, Wavelength 16.48cm
# sinewave.set_pitch(37)  # Note C#/Db7, Frequency 2217.46, Wavelength 15.56cm
# sinewave.set_pitch(38)  # Note D7, Frequency 2349.32, Wavelength 14.69cm
# sinewave.set_pitch(39)  # Note D#/Eb7, Frequency 2489.02, Wavelength 13.86cm
# sinewave.set_pitch(40)  # Note E7, Frequency 2637.02, Wavelength 13.08cm
# sinewave.set_pitch(41)  # Note F7, Frequency 2793.83, Wavelength 12.35cm
# sinewave.set_pitch(42)  # Note F#/Gb7, Frequency 2959.96, Wavelength 11.66cm
# sinewave.set_pitch(43)  # Note G7, Frequency 3135.96, Wavelength 11.00cm
# sinewave.set_pitch(44)  # Note G#/Ab7, Frequency 3322.44, Wavelength 10.38cm
# sinewave.set_pitch(45)  # Note A7, Frequency 3520.00, Wavelength 9.80cm
# sinewave.set_pitch(46)  # Note A#/Bb7, Frequency 3729.31, Wavelength 9.25cm
# sinewave.set_pitch(47)  # Note B7, Frequency 3951.07, Wavelength 8.73cm

# ==============Octave 8=================

# sinewave.set_pitch(48)  # Note C8, Frequency 4186.01, Wavelength 8.24cm
# sinewave.set_pitch(49)  # Note C#/Db8, Frequency 4434.92, Wavelength 7.78cm
# sinewave.set_pitch(50)  # Note D8, Frequency 4698.63, Wavelength 7.34cm
# sinewave.set_pitch(51)  # Note D#/Eb8, Frequency 4978.03, Wavelength 6.93cm
# sinewave.set_pitch(52)  # Note E8, Frequency 5274.04, Wavelength 6.54cm
# sinewave.set_pitch(53)  # Note F8, Frequency 5587.65, Wavelength 6.17cm
# sinewave.set_pitch(54)  # Note F#/Gb8, Frequency 5919.91, Wavelength 5.83cm
# sinewave.set_pitch(55)  # Note G8, Frequency 6271.93, Wavelength 5.50cm
# sinewave.set_pitch(56)  # Note G#/Ab8, Frequency 6644.88, Wavelength 5.19cm
# sinewave.set_pitch(57)  # Note A8, Frequency 7040.00, Wavelength 4.90cm
# sinewave.set_pitch(58)  # Note A#/Bb8, Frequency 7458.62, Wavelength 4.63cm
# sinewave.set_pitch(59)  # Note B8, Frequency 7902.13, Wavelength 4.37cm


sinewave.set_volume(7)

sinewave.play()

time.sleep(7)

sinewave.stop()

print("Sinewave Stops")
