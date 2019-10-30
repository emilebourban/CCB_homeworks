import numpy as np 
import matplotlib.pyplot as plt


def main():

    forces = []
    timestep = []
    start_time = []
    end_times = []
    seeds = []
    time_series = []

    with open('time_series.log') as file:
        for line in file:

            if line.startswith('Force'):
                line_list = line.strip().split()
                forces.append(float(line_list[1]))
                timestep.append(int(line_list[3]))
                start_time.append(int(line_list[5]))
                end_times.append(int(line_list[7]))
                seeds.append(int(line_list[9]))

            else:
                time_series.append(list(map(lambda x: float(x), line.strip().split())))

    time_series = np.array(time_series)
    print(time_series.shape)
    for i in range(time_series.shape[0]):
        plt.plot(time_series[i])
    plt.show()

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



if __name__ == '__main__':
    main()
