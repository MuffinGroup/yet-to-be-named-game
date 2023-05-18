import pickle
from os import path

world_data = [0, 0, 0]

if True:
	#save level data
	pickle_out = open(f'level1_data', 'wb')
	pickle.dump(world_data, pickle_out)
	pickle_out.close()

if path.exists(f'level1_data'):
		pickle_in = open(f'level1_data', 'rb')
		world_data = pickle.load(pickle_in)
		print(world_data)