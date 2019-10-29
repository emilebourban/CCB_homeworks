import os
import numpy as numpy



def get_lengths(means, stds):
    for f in os.listdir(os.getcwd()):
        if f == 'dmpcas.es1_sim':
            get_next_line = False
            for line in f:
                if get_next_line:
                    means.append(line.split()[0])
                    stds.append(line.split()[1])
                    return
                if line.startswith('Spring EE distance'):
                    get_next_line = True
            else:
                raise EOFError('No spring EE distance found')
    else:
        raise FileNotFoundError('dmpcas files not found')

