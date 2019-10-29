import numpy as np
import matplotlib.pyplot as plt


path = 'D:\\Utilisateurs\\Emile\\Documents\\MA3\\CCB\\CCB_homeworks\\homework1\\results.log'
data = np.loadtxt(path, skiprows=1)

plt.figure()
plt.errorbar(data[:,0], data[:,1], yerr=data[:,2], ecolor='k', elinewidth=0.7, capthick=0.7, capsize=2.5)
plt.title("Length-Force plot")
plt.show()