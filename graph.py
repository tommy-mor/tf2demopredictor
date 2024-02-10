import numpy as np

players = []

with open('./file.txt', 'r') as f:
    f.readline()
    f.readline()


    ticks = list()
    healths = list()

    while True:
        string = f.readline().strip()

        if 'Player: ' in string:
            players.append([ticks, healths])
            ticks = list()
            healths = list()
        elif string == '':
            break
        else:
            [tick, health] = string.split(': ')
            ticks.append(int(tick))
            healths.append(int(health))

        


import matplotlib.pyplot as plt

for [ticks, healths] in players:
    plt.plot(ticks, healths)

plt.xlabel('Tick')
plt.ylabel('Health')
plt.title('Health over time')
plt.show() 