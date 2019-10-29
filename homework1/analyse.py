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


for i, force in enumerate(forces):
    margin = 15
    start_ind = int(start_time[i]//timestep[i] + margin)
    end_ind = int(end_times[i]//timestep[i] - margin)

    mean = time_series[i,start_ind:end_ind].mean()
    std = time_series[i,start_ind:end_ind].std()
    print(force, mean, std)


