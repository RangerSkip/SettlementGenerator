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

		Settlement.filename = first+second

		Settlement.name = "Name: "+ first+second

	def create_size(self):
		population = random.randint(0, 4)
		people = random.randint(1, 10)

		if population == 0:
			#Farm
			Settlement.settlementType = "Type: "+Type.Settlement_Type[0]
			Settlement.population = "Population: "+str(random.randint(2,20))

		elif population == 1:
			#Hamlet
			Settlement.settlementType = "Type: "+Type.Settlement_Type[1]
			Settlement.population = "Population: "+str(people*10)

		elif population == 2:
			#Village
			Settlement.settlementType = "Type: "+Type.Settlement_Type[2]
			Settlement.population = "Population: "+str(people*100)

		elif population == 3:
			#Town
			Settlement.settlementType = "Type: "+Type.Settlement_Type[3]
			Settlement.population = "Population: "+str(people*1000)

		else:
			#City
			Settlement.settlementType = "Type: "+Type.Settlement_Type[4]
			Settlement.population = "Population: "+str(people*500+10000)

	def create_features(self):
		Settlement.features = "Notable Features: {}".format(random.choice(Features.Settlement_Features))

	def create_politics(self):
		Settlement.politics = "Politics: {}".format(random.choice(Politics.Settlement_Politics))

	def create_buildings(self):
		if Settlement.settlementType == 'Type: Farm':
			Settlement.buildings = Buildings.FBuildings
		elif Settlement.settlementType == 'Type: Hamlet':
			Settlement.buildings = Buildings.HBuildings
		elif Settlement.settlementType == 'Type: Village':
			Settlement.buildings = Buildings.VBuildings
		elif Settlement.settlementType == 'Type: Town':
			Settlement.buildings = Buildings.TBuildings
		else:
			Settlement.buildings = Buildings.CBuildings


	def create_purpose(self):
		var = random.randint(0, 10)

		if var <= 2:
			#Road/River Convergence
			Settlement.purpose = "Purpose: Road/River Convergence"
			Settlement.resources = "Resources: "+random.choice(Purpose.Trade_Resource)

		elif 3 <= var <= 5:
			#Natural Resource
			Settlement.purpose = "Purpose: Natural Resources"
			temp1 = random.choice(Purpose.Trade_Resource)
			temp2 = random.choice(Purpose.Trade_Resource)

			if temp1 == temp2:
				Settlement.resources = "Resources: "+temp1+". This land is doubly fertile and has a 50% chance to have rare or legendary crops/creatures/fuels."
			else:
				Settlement.resources = "Resources: "+temp1+" and "+temp2


		elif var == 6 or var == 7:
			#Mining Settlement
			Settlement.purpose = "Purpose: Mining Settlement"
			Settlement.resources = "Resources: "+random.choice(Purpose.Metal_Resouce)+" and "+random.choice(Purpose.Trade_Resource)

		else:
			#Military/Strategic Value
			Settlement.purpose = "Purpose: Military/Strategic Value"
			Settlement.resources = "Resources: "+random.choice(Purpose.Metal_Resouce)


def make_sure_path_exists(path):
	try:
		os.makedirs(path)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

MySettlements = []

make_sure_path_exists('Settlements')

user = int(input("How many settlements do you want? "))
for x in range(user):
	MySettlements.append(Settlement())
	filename = "Settlements/{}".format(MySettlements[x].filename)
	#print(filename)

	file = open(filename, 'w+')

	file.write(MySettlements[x].name + '\n')
	file.write(MySettlements[x].settlementType + '\n')
	file.write(MySettlements[x].population + '\n')
	file.write(MySettlements[x].politics + '\n')
	file.write(MySettlements[x].purpose + '\n')
	file.write(MySettlements[x].features + '\n')
	file.write(MySettlements[x].resources + '\n')
	file.write("Buildings: " + '\n')
	for elem in MySettlements[x].buildings:
		file.write(elem + '\n')
	file.write("Notes: \n")

	file.close()
