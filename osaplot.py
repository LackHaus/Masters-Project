import matplotlib.pyplot as plt
import os
from pathlib import Path
import numpy as np

folder_path = Path('2022-06-22 POC4 MIT material annealed at LMF/cells456')

xs = []
ys = []
files = []

for file in os.listdir(folder_path):
    if 'ref' in file:
        y_ref = []
        f = open(folder_path / Path(file))
        data = f.readlines()[10:]
        for i in data:
            y_ref.append(float(i.split('\t')[1]))

y_ref = np.array(y_ref)

for file in os.listdir(folder_path):
    if 'ref' not in file:
        x = []
        y = []
        files.append(file)
        f = open(folder_path / Path(file))
        data = f.readlines()[10:]
        for i in data:
            x.append(float(i.split('\t')[0]))
            y.append(float(i.split('\t')[1]))

        x = np.array(x)
        y = y_ref - np.array(y)
        xs.append(x)
        ys.append(-1*y)

for i in range(len(xs)):
    plt.plot(xs[i], ys[i])

plt.legend(files)
#plt.legend(['Alignment loop', 'Drop PCM 1', 'Drop PCM 2', 'Drop PCM 3', 'Through', 'ref. source'])
plt.xlabel('Wavelength [nm]')
plt.ylabel('Losses [dB]')
plt.show()