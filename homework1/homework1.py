import os
import sys
import subprocess


def get_ee_length():
    
    eel_files = [file for file in os.listdir() if file.startswith('eeldata')]
    eel = []

    for i, file in enumerate(eel_files):
        with open(file, 'rt') as f:
            for line in f:
                if len(line.strip().split()) > 0:
                    eel.append(line.strip().split())

    return eel


def clean_cwd():

    # Generator of the files generated for each runs
    del_files = (file for file in os.listdir() if file.endswith('.vtk')
                 or file.endswith('.dat')
                 or file.startswith('eeldata'))

    for file in del_files:
        try:
            os.remove(file)
            print("\rRemoved {:s} succesfully!".format(file),end=' '*5)
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
                    next(rf)

                else:
                    wf.write(line)


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


def main():
    #Removes previous simulation files
    clean_cwd()

    for force in range(0, 100, 10):
        change_force('dmpci.es1', force)

        # Starts simulation
        subprocess.run(r"./dpd-w10.exe es1_sim")

        #Get EE length

    eel = get_ee_length()
    print(eel)


if __name__ == "__main__":
    main()
