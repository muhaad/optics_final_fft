import numpy
from numpy import fft
import matplotlib.pyplot as plt
import math

file_name = '2_3_Mixed.CSV'

sample_interval = .001      #samples taken every milisecond for 2.5 seconds
sample_freq = 1/sample_interval     #sample frequency in hertz

y_offset = -8*10**(-3)
y_scale = 5*10**(-2)

test_freq = 300        #test frequency for debugging

time = []       
volt = [] #voltage in millivolts
time_domain_shift = 0

with open(file_name, 'r') as f:
    lines = f.readlines()
    for line in lines:
        data = line.split(',')
        if(len(time) == 0):
            time_domain_shift = float(data[0].strip())

        time.append(float(data[0].strip()) - time_domain_shift)
        #volt.append(float(data[1].strip())*y_scale)        #comment out this line when populating volt[] with sine wave
        volt.append(math.sin(sample_interval*len(volt)*2*3.14*test_freq))   #sample sin wave to debug fft
      

plt.plot(time, volt)    #Time domain 
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (Volts)")
plt.show()
        
freq = fft.rfft(volt)   #Real fft algorithim
mag= []                 #Magnitude of frequency 

#print("Number of Time Steps: ", len(time))

for i in freq:
    mag.append(abs(i))

fft_size = len(mag)     #number of frequency bins

#freq_resolution = sample_freq/fft_size      #frequency resolution of fft

freq_resolution = sample_freq/len(time)

print("frequency resolution: ", freq_resolution)

x_axis = numpy.arange(0, freq_resolution*fft_size, freq_resolution) #x-axis of fft

   
#print(len(x_axis))

plt.plot(x_axis, mag)
plt.xlabel("Frequency (Hertz)")
plt.ylabel("Magnitude")
plt.show()

##The below code just plots the lower frequencies##

x_axis_short = []
mag_short = []

for i in range(100):
    x_axis_short.append(x_axis[i])
    mag_short.append(mag[i])

plt.plot(x_axis_short, mag_short)
plt.xlabel("Frequency (Hertz)")
plt.ylabel("Magnitude")
plt.show()



    







