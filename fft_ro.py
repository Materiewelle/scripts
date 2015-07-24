import numpy
import matplotlib.pyplot as plt

V = []
dt = 2e-15

file = open("2.strip")
m = 0
for line in file:
    V.append(float(line.strip("\n")))

    
A = numpy.fft.rfft(V)
f = numpy.fft.rfftfreq(len(V), dt) * 1e-12
t = numpy.linspace(0, len(V) * dt, len(V))

plt.plot(t * 1e12, V)
#plt.xlim([20, 400])
#plt.ylim([-0.5, 1])
plt.title("TFET ring oscillator: transient signal")
plt.xlabel("$t$ / ps")
plt.ylabel("$V_{out}$ / V") 
plt.show()

plt.plot(f, numpy.absolute(A))
plt.xlim([1, 50])
#plt.ylim([-0.5, 1])
plt.title("TFET ring oscillator: FFT")
plt.xlabel("$f$ / THz")
plt.ylabel("FFT$(V_{out})$") 
plt.show()
