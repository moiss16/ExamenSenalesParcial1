import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

#Frecuenciasx 
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia852 = SinSignal(freq=852, amp=1, offset=0)

#Frecuenciasy
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)

frecuencia_numero7 = frecuencia852 + frecuencia1209 
frecuencia_numero9 = frecuencia852 + frecuencia1477 
frecuencia_numero4 = frecuencia770 + frecuencia1209 

#Waves
wave_7 = frecuencia_numero7.make_wave(duration=0.5, start=0, framerate=44100)
wave_9 = frecuencia_numero9.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_4 = frecuencia_numero4.make_wave(duration=0.5, start=1, framerate=44100)
wave_7_2 = frecuencia_numero7.make_wave(duration=0.5, start=1.5, framerate=44100)


#outputs
wave_final = wave_7 + wave_9 + wave_4 + wave_7_2


wave_final.write("output_final.wav")