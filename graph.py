import numpy as np

import sys

def read_file(fname):
    redplayers = []
    bluplayers = []

    with open(fname, 'r') as f:
        f.readline()
        f.readline()


        ticks = list()
        healths = list()

        while True:
            string = f.readline().strip()

            if 'Player:' in string:
                [_, team, player] = string.split(':')
                if team == 'Red':
                    redplayers.append([ticks, healths])
                else:
                    bluplayers.append([ticks, healths])

                ticks = list()
                healths = list()
            elif string == '':
                break
            else:
                [tick, health] = string.split(': ')
                ticks.append(int(tick))
                healths.append(int(health))


        max_length = 99999999999
        for [ticks, healths] in bluplayers:
            max_length = min(max_length, ticks[-1])

        for [ticks, healths] in redplayers:
            max_length = min(max_length, ticks[-1])

        print(max_length)
        data = np.ndarray(shape=(2, 6, max_length))

        for i, [ticks, healths] in enumerate(bluplayers[:6]):
            # set plt color 

            #plt.plot(healths, color='blue')
            data[0][i] = np.array(healths)[:max_length]

        for i, [ticks, healths] in enumerate(redplayers[:6]):
            #plt.plot(healths, color='red')
            data[1][i] = np.array(healths)[:max_length]

        return data

        
if __name__ == '__main__':
    data = read_file(sys.argv[1])
    data.tofile(sys.argv[1] + '.bin')