import numpy as np
import matplotlib.pyplot as plt 

path = 'D:\\Utilisateurs\\Emile\\Documents\\MA3\\CCB\\CCB_homeworks\\homework1\\'

times = []
lengths = []


with open(path+'dmpchs.es1') as file:
    for line in file:
        times.append(int(line.split()[0]))
        lengths.append(float(line.split()[-1]))


force = 100
with open(path+'time_series.log', 'at') as file:
    file.write('\nForce: {}\tTimestep: {}\n{}'.format(force, times[0],'\t'.join(['{:<8.5f}'.format(el) for el in lengths])))


plt.figure()
plt.plot(times, lengths)
plt.show()




