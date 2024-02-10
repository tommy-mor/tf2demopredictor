import numpy as np


redplayers = []
bluplayers = []

with open('./file.txt', 'r') as f:
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

        


import matplotlib.pyplot as plt

max_length = 99999999999
for [ticks, healths] in bluplayers:
    max_length = min(max_length, ticks[-1])

for [ticks, healths] in redplayers:
    max_length = min(max_length, ticks[-1])

print(max_length)
data = np.ndarray(shape=(2, 6, max_length))


for i, [ticks, healths] in enumerate(bluplayers):
    # set plt color 

    #plt.plot(healths, color='blue')
    data[0][i] = np.array(healths)[:max_length]

for i, [ticks, healths] in enumerate(redplayers):
    #plt.plot(healths, color='red')
    data[1][i] = np.array(healths)[:max_length]


plt.plot(data[0].sum(axis=0), color='blue')
plt.plot(data[1].sum(axis=0), color='red')
plt.xlabel('Tick')
plt.ylabel('Health')
plt.title('Health over time')
plt.show() 