import numpy as np
import matplotlib.pyplot as plt

temperature = np.arange(10,80,5)
numbering = np.arange(1,15)
real_temp = [12.66,16.26,19.81,23.62,27.46,31.34,34.78,38.51,42.57,45.21,49.57,53.31,55.89,60.98]
#
#for num in numbering:
#    astring = "{:03}_{}C.txt".format(num,temperature[num-1])
#    data = np.loadtxt(astring, delimiter = None)
#
#    realimp = data[:,0]
#    imagimp = data[:,1]
#    freq = data[:,2]
#
#    plt.figure()
#    plt.rc("text", usetex = True)
#    plt.rc("font", family = "serif")
#    plt.plot(realimp, -imagimp,label = "{}".format(temperature[num-1]))
#
#    plt.xlabel(r"$$Re\left(Z\right)$$")
#    plt.ylabel(r"$$-Im\left(Z\right)$$")
#    plt.title("Impedance Plot {} Celcius".format(temperature[num-1]))
#    plt.legend()
#    plt.savefig("{:03}_{}C.png".format(num,temperature[num-1]), format = "png", dpi = 1200)
#    plt.show()


for number in numbering:
    bstring = "{:03}_{}C.txt".format(number,temperature[number-1])
    data = np.loadtxt(bstring, delimiter = None)
    realimp = data[:,0]
    imagimp = data[:,1]
    freq = data[:,2]
    plt.plot(realimp, -imagimp, "s-", label = "{}".format(real_temp[number-1]))
#plt.rc("text", usetex = True)
#plt.rc("font", family = "serif")
#plt.xlabel(r"$$Re\left(Z\right)$$")
#plt.ylabel(r"$$-Im\left(Z\right)$$")
plt.xlabel("Re(Z) (Ohm)")
plt.ylabel("-Im(Z) (Ohm)")
plt.title("Impedance Plot in Celcius of MAPI 0.625 M")
plt.legend(bbox_to_anchor = (1.0, 1.05))
plt.savefig("overall.png", format = "png", dpi = 1200, bbox_inches = "tight")
plt.show()
