import numpy as np
import matplotlib.pyplot as plt
from plotstuff import colours
cols = colours()

plotpar = {'axes.labelsize': 18,
            'font.size': 18,
            'legend.fontsize': 18,
            'xtick.labelsize': 18,
            'ytick.labelsize': 18,
            'text.usetex': True}
plt.rcParams.update(plotpar)

data = np.genfromtxt("isochrones/UBVRIJHKsKp/fehm05afem2.UBVRIJHKsKp",
                     skip_header=9).T
logTeff = data[2]
logL = data[4]
c = 278
logLs, logTeffs = [], []
for i in range(int(len(logL)/float(c))):
    logLs.append(logL[c*i:c*(i+1)])
    logTeffs.append(logTeff[c*i:c*(i+1)])
logLs = np.array(logLs)

solar_luminosity = 3.828e26  # watts
L = solar_luminosity * 10**(logLs)

colors = [cols.blue, cols.pink, cols.orange, cols.green, cols.purple,
          cols.lightblue, cols.red, cols.turquoise]
plt.clf()
for i in range(5):
    plt.plot(10**logTeffs[i][:-100], logLs[i][:-100], colors[i])
plt.xlim(4500, 10000)
plt.xlabel("$T_{\mathrm{eff}}$")
plt.ylabel("$\log(L / L_\odot)$")
plt.savefig("isochrone_example")
