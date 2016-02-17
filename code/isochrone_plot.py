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
colors = [cols.blue, cols.pink, cols.orange, cols.green, cols.purple,
          cols.lightblue, cols.red, cols.turquoise]


def all_isochrones():
    # data = np.genfromtxt("isochrones/UBVRIJHKsKp/fehp00afep2.UBVRIJHKsKp",
    data = np.genfromtxt("isochrones/UBVRIJHKsKp/fehm05afem2.UBVRIJHKsKp",
                         skip_header=9).T
    logTeff = data[2]
    logL = data[4]
    c = 278
    logLs, logTeffs = [], []
    for i in range(int(len(logL)/float(c))):
        logLs.append(np.array(logL[c*i:c*(i+1)]))
        logTeffs.append(np.array(logTeff[c*i:c*(i+1)]))

    # logLs = np.array(logLs)
    # solar_luminosity = 3.828e26  # watts
    # L = solar_luminosity * 10**(logLs)

    plt.clf()
    for i in range(len(logLs)-1):
        # plt.plot(10**logTeffs[i][:-100], logLs[i][:-100], colors[i])
        plt.plot(10**logTeffs[i][:-100], logLs[i][:-100])
    plt.plot(5778, 0, "ko")
    plt.xlim(4500, 10000)
    plt.xlabel("$T_{\mathrm{eff}}$")
    plt.ylabel("$\log(L / L_\odot)$")
    plt.savefig("isochrone_example")


def solar_age():
    # data = np.genfromtxt("isochrones/tmp1455615536.iso", skip_header=9).T
    data = np.genfromtxt("isochrones/tmp1455615814.iso", skip_header=9).T
    logTeff = data[2]
    logL = data[4]
    M = data[1]
    m = (.9 < M) * (M < 1.1)
    print(M[m])
    solar_luminosity = 3.828e26  # watts
    L = 10 ** logL

    plt.clf()
    plt.plot(10**logTeff[m], L[m], "r.")
    plt.plot(5778, 1, "ko")
    plt.xlim(4500, 10000)
    plt.xlabel("$T_{\mathrm{eff}}$")
    plt.ylabel("$\log(L / L_\odot)$")
    plt.savefig("isochrone_solar")

if __name__ == "__main__":
    solar_age()
