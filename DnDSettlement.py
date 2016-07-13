import errno
import os
import random
import sys
from database import Buildings, Features, Names, Politics, Purpose, Type

"""
Functionality of this Program:
	Allow user to create as many settlements as they want.
	Output of each settlement is saved to a textfile, the name of which is the settlement
		Settlements put in a folder labeled "Settlements"
	Output is as follows:

		Name:
		Settlement Type: (Farm, Hamlet, etc)
		Population:
		Politics:
		Purpose:
		Notable Features:
		Resources:
		Buildings:
		Notes:

	Created by Victor Gavojdea, 2016
"""

class Settlement:

	def __init__(self):
		self.create_name()
		self.create_size()
		self.create_politics()
		self.create_features()
		self.create_buildings()
		self.create_purpose()
		name = ""
		settlementType = ""
		population = 1
		politics = ""
		purpose = ""
		features = ""
		resources = ""
		buildings = ""
		filename = ""

	def create_name(self):
		first = random.choice(Names.First_Name)
		second = random.choice(Names.Second_Name)

		self.filename = first+second

		self.name = "Name: {}".format(first+second)

	def create_size(self):
		population = random.randint(0, 4)
		people = random.randint(1, 10)

		pops = {
			'Farm': lambda: people,
			'Hamlet': lambda: people*10,
			'Village': lambda: people*100,
			'Town': lambda: people*1000,
			'City': lambda: people*500+10000
		}

		kind, pop = random.choice(list(pops.items()))

		self.settlementType = "Type: {}".format(kind)
		self.population = "Population: {}".format(pop())


	def create_features(self):
		self.features = "Notable Features: {}".format(random.choice(Features.Settlement_Features))

	def create_politics(self):
		self.politics = "Politics: {}".format(random.choice(Politics.Settlement_Politics))

	def create_buildings(self):
		self.buildings = Buildings.string_to_buildings[self.settlementType]

	def create_purpose(self):
		var = random.randint(0, 10)

		if var <= 2:
			#Road/River Convergence
			self.purpose = "Purpose: Road/River Convergence"
			self.resources = "Resources: {}".format(random.choice(Purpose.Trade_Resource))

		elif 3 <= var <= 5:
			#Natural Resource
			self.purpose = "Purpose: Natural Resources"
			temp1 = random.choice(Purpose.Trade_Resource)
			temp2 = random.choice(Purpose.Trade_Resource)

			if temp1 == temp2:
				self.resources = "Resources: {}. This land is doubly fertile and has a 50% chance to have rare or legendary crops/creatures/fuels.".format(temp1)
			else:
				self.resources = "Resources: {} and {}".format(temp1, temp2)


		elif var == 6 or var == 7:
			#Mining Settlement
			self.purpose = "Purpose: Mining Settlement"
			self.resources = "Resources: {} and {}".format(random.choice(Purpose.Metal_Resouce) ,random.choice(Purpose.Trade_Resource))

		else:
			#Military/Strategic Value
			self.purpose = "Purpose: Military/Strategic Value"
			self.resources = "Resources: ".format(random.choice(Purpose.Metal_Resouce))


def make_sure_path_exists(path):
	try:
		os.makedirs(path)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

MySettlements = []

make_sure_path_exists('Settlements')

while True:
	try:
		num_input = int(input("How many settlements do you want? "))
		break
	except ValueError:
		print("Not a valid integer")

for x in range(num_input):
	MySettlements.append(Settlement())
	filename = "Settlements/{}".format(MySettlements[x].filename)
	#print(filename)

	with open(filename, 'w+') as f:
		f.write(MySettlements[x].name + '\n')
		f.write(MySettlements[x].settlementType + '\n')
		f.write(MySettlements[x].population + '\n')
		f.write(MySettlements[x].politics + '\n')
		f.write(MySettlements[x].purpose + '\n')
		f.write(MySettlements[x].features + '\n')
		f.write(MySettlements[x].resources + '\n')
		f.write("Buildings: " + '\n')
		for elem in MySettlements[x].buildings:
			f.write('\t' + elem + '\n')
		f.write("Notes: \n")
