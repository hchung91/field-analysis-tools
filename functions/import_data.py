import numpy as np 

def import_data(filename, skiprows = 1):
	imported = np.loadtxt(filename, skiprows = skiprows)

	points = imported[0:, 0:3]
	data = imported[0:, 3:]

	if data.shape[1] == 2:
		data = np.array([data[0:, 0] + data[0:, 1]*1j]).transpose()
	
	elif data.shape[1] == 6:
		data = np.array([data[0:, 0] + data[0:, 1]*1j, \
                     data[0:, 2] + data[0:, 3]*1j, \
                     data[0:, 4] + data[0:, 5]*1j]).transpose()

	return data
