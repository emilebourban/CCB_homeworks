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

    for i, force in enumerate(forces):
        margin = 15
        start_ind = int(start_time[i]//timestep[i] + margin)
        end_ind = int(end_times[i]//timestep[i] - margin)

        mean = time_series[i,start_ind:end_ind].mean()
        std = time_series[i,start_ind:end_ind].std()
        print(force, mean, std)


if __name__ == '__main__':
    main()
