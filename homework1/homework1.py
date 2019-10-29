import os
import sys
import subprocess

import numpy as np


def clean_cwd():

    # Generator of the files generated for each runs
    del_files = (file for file in os.listdir() if file.endswith('.vtk')
                 or file.endswith('.dat')
                 or file.startswith('eeldata')
                 or file.endswith('.log'))

    for file in del_files:
        try:
            os.remove(file)
            print("\rRemoved {:s} succesfully!".format(file), end=' '*15)
        except:
            print("\rFailed to remove {:s}".format(file))
            raise

    print('')
    
    
def change_force(filename, force):

    try:
        os.remove(filename+'_sim')
    except IOError:
        print('No previous simulation file')
    
    with open(filename, 'rt') as rf:
        with open(filename+'_sim', 'wt') as wf:

            for line in rf:
                if line.startswith('Command ConstantForceOnTarget'):
                    for sign in [1, -1]:
                        # Copies current line
                        c_line = line
                        c_line = c_line.strip().split()
                        c_line[-1] = sign *force

                        # Converts list to list[str]
                        c_line = list(map(lambda x: str(x), c_line))

                        wf.write('\t'.join(c_line) +'\n')

                        # Gets next line
                        line = next(rf)

                else:
                    wf.write(line)


def get_lengths(filename, means, stds):

    with open(filename, 'rt') as f:
        for line in f:
            if line.startswith('Spring EE distance'):

                line = next(f)
                means.append(float(line.split()[0]))
                stds.append(float(line.split()[1]))
                return

        else:
            raise EOFError('No spring EE distance found')


def main():
    #Removes previous simulation files
    clean_cwd()
    # Creates to store the simulation values
    with open('results.log', 'wt') as f:
        f.write("{:<8s}\t{:<8s}\t{:<8s}\n".format("Force", "Mean", "Std"))
    
    means = []
    stds = []
    forces = np.linspace(0, 100, 10)
    for i in range(forces.shape[0]):
        change_force('dmpci.es1', forces[i])

        # Starts simulation
        subprocess.run(r"./dpd-w10.exe es1_sim")

        #Get EE length
        get_lengths('dmpcas.es1_sim', means, stds)

        with open('results.log', 'a') as f:
            f.write("{:<8.5f}\t{:<8.5f}\t{:<8.5f}\n".format(float(forces[i]), means[-1], stds[-1]))
        print(means, stds)


if __name__ == "__main__":
    main()
