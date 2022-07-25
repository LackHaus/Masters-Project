import matplotlib.pyplot as plt
import os
from pathlib import Path
import numpy as np

folder_path = Path('E:/PCM/Testing Setup/Data/2022-07-25_PCMtestchip as recieved')

xs = []
ys = []
files = []

for file in os.listdir(folder_path):
	
	with open(folder_path / file) as f:
		if "ref" in file:
			datas = []
			data = f.readlines()
			for i in data:
				datas.append(i.split('\t'))
			x_ref = []
			y_ref = []
			for i in datas:
				x_ref.append(float(i[0]))
				y_ref.append(float(i[1]))

		else:
			files.append(file)
			datas = []
			data = f.readlines()
			for i in data:
				datas.append(i.split('\t'))
			x = []
			y = []
			for i in datas:
				x.append(float(i[0]))
				y.append(float(i[1]))
			xs.append(x)
			ys.append(y)

print(files)
title = str(folder_path).split("Data")[-1]

for i in range(len(xs)):
	plt.plot(np.array(xs[i]), np.array(ys[i])-np.array(y_ref))


plt.title(title)
plt.xlabel("Wavelength [nm]")
plt.ylabel("Losses [dB]")
plt.legend(files)
plt.show()



