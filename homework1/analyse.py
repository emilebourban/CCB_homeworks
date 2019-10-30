import numpy as np 
import matplotlib.pyplot as plt


forces = []
timestep = []
start_time = []
end_times = []
seeds = []
time_series = []

with open('time_series.log') as file:
    for line in file:
        if line.startswith('Force'):
            forces.append(float(line.strip().split()[1]))
            timestep.append(int(line.strip().split()[3]))
            start_time.append(int(line.strip().split()[5]))
            end_times.append(int(line.strip().split()[7]))
            seeds.append(int(line.strip().split()[9]))
        else:
            time_series.append(list(map(lambda x: float(x), line.strip().split())))

time_series = np.array(time_series)

forces_set = set(forces)

margin = 20

results = []

for force in forces_set:
    temp = []
    for i, f in enumerate(forces):
        if force == f:
            
            start_ind = int(start_time[i]//timestep[i] + margin)
            end_ind = int(end_times[i]//timestep[i] - margin)

            temp.append(time_series[i,start_ind:end_ind].mean())
            # std = time_series[i,start_ind:end_ind].std()
    temp = np.array(temp)
    results.append([force, temp.mean(), temp.std()])

results = np.array(results)
# plot force vs length with std
plt.figure()
plt.errorbar(results[:,0], results[:,1], yerr=results[:,2], ecolor='k', elinewidth=0.7, capthick=0.7, capsize=2)
plt.title("Length-Force plot")
plt.show()