#!/usr/bin/env python

from chroma.geometry import Material

import pandas as pd
import random

# read materials from database
# randomize functionality

class material_manager:
	def __init__(self,run_id):
		# self.material_data_path = '/home/chroma/chroma_fresh_start/data_files/bulk_materials.csv'
		# self.material_data_path = '/home/chroma/chroma_fresh_start/results/data/copperplates_06.23.2022/bulk_materials _copperplates_06232022.csv'
		# self.material_data_path = '/home/chroma/chroma_fresh_start/results/data/beam_direction_06.30.2022/bulk_materials _copperplates_06302022.csv'
		# self.material_data_path = '/home/chroma/chroma_fresh_start/results/data/silica_window_07.18.2022/bulk_materials _silica_window_07182022.csv'
		# self.material_data_path = '/home/chroma/chroma_fresh_start/results/data/source_copperholder_08.16.2022/bulk_materials __sourceCu_holder_08162022.csv'
		# self.material_data_path = '/home/chroma/chroma_fresh_start/results/data/copper_gasket_08.29.2022/bulk_materials _coppergasket_08292022.csv'
		# self.material_data_path = '/home/chroma/chroma_fresh_start/results/data/Al_filler_02.07.2023/bulk_materials _Alfiller_02072023.csv'
		# self.material_data_path = '/home/chroma/chroma_fresh_start/results/data/sourcepart_05.11.2023/bulk_materials _sourcepart_05112023.csv'
		# self.material_data_path ='/home/chroma/chroma_fresh_start/results/data/Sebastian_teflon_05.12 .2023/bulk_materials _Sebastian_teflon_0512.csv'
		# self.material_data_path = '/home/chroma/chroma_fresh_start/results/data/Sebastian_teflon_05.23.2023/bulk_materials _Sebastian_teflon_0523.csv'
		# self.material_data_path = '/home/chroma/chroma_fresh_start/results/data/Sebastian_teflon_upperlimit_06.05.2023/bulk_materials _Sebastian_teflon_upper_0605.csv'
		# self.material_data_path = '/home/chroma/chroma_fresh_start/results/data/Sebastian_flippedsource_06.06.2023/bulk_materials _Sebastian_teflon_FS_0606.csv'
		# self.material_data_path = '/home/chroma/chroma_fresh_start/results/data/Sebastian_FS_06.08.2023_correctedSiPM/bulk_materials _Sebastian_teflon_FS_0608_corrected.csv'
		# self.material_data_path = '/home/chroma/chroma_fresh_start/results/data/Sebastian_03.31.2023(liquefaction_corrrectedSiPM)/bulk_materials _Sebastian_03312023_corrected.csv'
		# self.material_data_path ='/home/chroma/chroma_fresh_start/results/data/Sebastian_05.18.2023(liquefaction)_correctedSiPM/bulk_materials _Sebastian_teflon_0518_corrected.csv'
		# self.material_data_path ='/home/chroma/chroma_fresh_start/results/data/Sebastian_07.20.2022(liquefaction)_corrrectedSiPM/bulk_materials _Sebastian_07202022_corrected.csv'
		self.material_data_path = '/home/chroma/chroma_fresh_start/results/data/Sebastian_08.01.2023(liquefaction)_correctedSiPM/bulk_materials _Sebastian_Pdreflector_0801_corrected.csv'

		self.run_id = run_id
		# self.savedata_path = '/home/chroma/chroma_fresh_start/results/data/Sebastian_FS_06.08.2023_correctedSiPM/datapoints/Cu_reflector_etal_vary_Cu_eta_LXe_eta.csv'
		self.savedata_path ='/home/chroma/chroma_fresh_start/results/data/Sebastian_08.01.2023(liquefaction)_correctedSiPM/datapoints/Si_reflector_vary_Si_eta_LXe_eta.csv'
		self.build_materials(run_id)
		self.global_material = self.materials['liquid xenon']

	def add_attributes(self,
				curr_material,
				refractive_index = None,
				absorption_length = None,
				scattering_length = None,
				density = 0.0):
		#set the optical index grabbed from csv file for simulation
		curr_material.set('refractive_index', refractive_index) 
		curr_material.set('absorption_length', absorption_length) 
		curr_material.set('scattering_length', scattering_length)
		curr_material.density = density

		# print(refractive_index)
		# return refractive_index

	def build_materials(self,run_id):
		# read in the csv file into dataframe
		self.materials_df = pd.read_csv(self.material_data_path)
		#print(self.materials_df)
		# iterate through all materials and create Material object, store into dictionary of materials
		self.materials = {}
		self.material_props = {}
		properties = self.materials_df.columns
		for index, row in self.materials_df.iterrows():
			curr_name = row['name'] #name of the material		
			self.materials[curr_name] = Material(name = curr_name)	
			# # # below define material properties without referring to the material property csv
			# if curr_name == 'silicon':
			# 	# column = ['Cu eta']
			# 	# copper_eta_ = pd.read_csv(self.savedata_path,usecols=column).to_numpy()
			# 	# copper_eta_all = copper_eta_.flatten()
			# 	# copper_eta = copper_eta_all[self.run_id]
			# 	# row['eta'] = round(random.uniform(0.72553,0.96400),4)
			# 	# row['eta'] = copper_eta
			# 	row['k'] = round(random.uniform(1.7223,2.0872),4)
			# # 	row['k'] = 1.413
			# 	print('silicon k',row['k'])



			# if curr_name == 'liquid xenon':	
			# # # # 	column = ['LXe Index of Refraction']
			# # # # 	LXe_eta_ = pd.read_csv(self.savedata_path,usecols=column).to_numpy()
			# # # # 	LXe_eta_all = LXe_eta_.flatten()
			# # # # 	LXe_eta = LXe_eta_all[self.run_id]
			# # # 	# row['refractive_index'] = round(random.uniform(1.59,1.78),4)
			#  	row['refractive_index'] = 1.60+(run_id)*0.01
			#  	print('LXe',row['refractive_index'])
			#  	# row['refractive_index'] = 1.69
			# # 	#row['refractive_index'] = LXe_eta
				

			# if curr_name == 'silicon':
			# 	row['eta'] = pd.read_csv('/home/chroma/Downloads/Silicon_Refractive_Indices.csv', usecols = ['n']).to_numpy().flatten()[run_id]
			# 	print(row['eta'])
			# 	row['k'] = pd.read_csv('/home/chroma/Downloads/Silicon_Refractive_Indices.csv', usecols = ['k']).to_numpy().flatten()[run_id]
			# 	print(row['k'])

			# if curr_name == 'copper':
			# 	row['eta'] = pd.read_csv('/home/chroma/chroma_fresh_start/data_files/Werner_Cu_Refractive_Indices.csv', usecols = ['n']).to_numpy().flatten()[run_id]
			# 	print('Cu',row['eta'])
			# 	row['k'] = pd.read_csv('/home/chroma/chroma_fresh_start/data_files/Werner_Cu_Refractive_Indices.csv', usecols = ['k']).to_numpy().flatten()[run_id]
			# 	print('Cu',row['k'])

			self.add_attributes(self.materials[curr_name],
								#refractive_index = r_i,
								#refractive_index = row['refractive_index']+random.uniform(-row['abs(r_i_error)'],row['abs(r_i_error)']), # only used when no surface model is defined
								refractive_index = row['refractive_index'],
								absorption_length = row['absorption_length'],
								scattering_length = row['scattering_length'],
								density = row['density'])

			self.material_props[curr_name] = dict(row)
			# print('material props',self.material_props)
			# try to update the real refractive_index to the csv. file
		# print(self.materials)



	def get_material(self, material_name):
		# check to see if material exists. if not, throw exception
		if material_name in self.materials:
			return self.materials[material_name]
		else:
			raise Exception('Material does not exist: ' + material_name)