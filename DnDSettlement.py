import errno
import os
import random
import sys

"""
Functionality of this Program:
	Allow user to create as many settlements as they want.
	Output of each settlement is saved to a textfile, the name of which is the settlement
		Settlements put in a folder labeled "Settlements"
	Output is as follows:

		Name:
		Settlement Type: (Farm, Hamlet, etc)
		Population:
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
		self.create_features()
		self.create_buildings()
		self.create_purpose()
		name = ""
		settlementType = ""
		population = 1
		purpose = ""
		resources = ""
		buildings = ""
		features = ""
		filename = ""

	First_Name = [
		"Ald",
		"All",
		"Alm",
		"Als",
		"Alt",
		"Ammer",
		"An",
		"And",
		"Arm",
		"Arn",
		"Aschen",
		"Ascher",
		"Aval",
		"Bel",
		"Bens",
		"Birn",
		"Blanken",
		"Blau",
		"Blut",
		"Bögen",
		"Borken",
		"Braun",
		"Brith",
		"Büche",
		"Calen",
		"Caras",
		"Diep",
		"Dol",
		"Dun",
		"Dunkel",
		"East ",
		"Ed",
		"Eis",
		"Elda",
		"Ell",
		"Eria",
		"Es",
		"Eschen",
		"Eth",
		"For",
		"Foro",
		"Fried",
		"Fürsten",
		"Gala",
		"Geis",
		"Gelb",
		"Giessen",
		"Gond",
		"Gor",
		"Grab",
		"Gräten",
		"Grau",
		"Gros",
		"Gruft",
		"Grün",
		"Günz",
		"Hagel",
		"Hall",
		"Har",
		"Hart",
		"Haven of ",
		"Hauzen",
		"Hech",
		"Herbst",
		"Herz",
		"Hohen",
		"Holz",
		"Hyara",
		"Ilmen",
		"Kall",
		"Klage",
		"Klein",
		"Lauffen",
		"Lauter",
		"Lin",
		"Lipp",
		"Loth",
		"Main",
		"Marien",
		"Mith",
		"Merse",
		"Mess",
		"Moos",
		"Mor",
		"Naum",
		"Nenn",
		"Neider",
		"Nin",
		"Nog",
		"Nord",
		"Obel",
		"Ober",
		"Ondo",
		"Orro"
		"Ost",
		"Oster",
		"Otters",
		"Pela",
		"Pfaffen",
		"Pfarr",
		"Pfeffen",
		"Rain",
		"Riesen",
		"Riven",
		"Romen",
		"Saal",
		"Salz",
		"Schaf",
		"Schöne",
		"Schroben",
		"Schwab",
		"Schwan",
		"Schwarz",
		"Semmen",
		"Sim",
		"Sommer",
		"Sonder",
		"South ",
		"Speeger",
		"Starn",
		"Stein",
		"Süd",
		"Tauber",
		"Taufel",
		"Tar",
		"Thar",
		"Thurin",
		"Tier",
		"Tiri",
		"Tränen",
		"Trost",
		"Under",
		"Up",
		"Upfen",
		"Val",
		"Vater",
		"Vecker",
		"Vin",
		"Wall",
		"Waren",
		"Way",
		"Wein",
		"Weiss",
		"West",
		"Winter",
		"Teeth of "
	]

	Second_Name = [
		"acker [field]",
		" Amroth"
		"ador",
		"andor",
		"argir",
		"bach [brook]",
		"bad",
		"berg [mountain]",
		"bourn",
		"burg",
		"brücke [bridge]",
		"brunnen [well]",
		"burg [town]",
		"chen [~small]",
		"damos",
		"dell",
		"duin",
		"dolin",
		"dolos",
		" Doras",
		"dorf [village]",
		"falas",
		"feld [field]",
		"field",
		"fort [fort]",
		"galgen [gallows]",
		"garost",
		"garoth",
		"gost",
		"grod",
		" Halad",
		"harrow",
		"haus [house]",
		"hausen [~retreat]",
		"heide [moor]",
		"heim [home]",
		"hellond",
		"hir",
		"hof [court]",
		"holz [woods]",
		"horst [nest]",
		"hügel [hill]",
		"hat [hut]",
		"hütte [cottage]",
		"labas",
		"leben [life]",
		"lembel",
		"lindon",
		"lond",
		"maida",
		"maldar",
		"monos",
		"menelos",
		"münde [river mouth]",
		"Maedhros",
		"nost",
		"schweig [~silence]",
		" Sirion",
		"stadt [town]",
		"star",
		"stätte [site, place]",
		"stein [stone]",
		"storni",
		"talmar",
		"thombar",
		"thar",
		"tirith",
		"tür [door]",
		"yamar",
		"wald [forest]",
		"wasser [water]",
	]

	Settlement_Type = [
		"Farm",
		"Hamlet",
		"Village",
		"Town",
		"City"
	]

	Settlement_Features = [
		"Arms (weapons, armor or gunsmiths)",
		"Books",
		"Brewing",
		"Center of learning",
		"Crumbling ramparts or palisade",
		"Eerie ruin on the edge of the settlement",
		"Famous for a yearly feast or festival",
		"Famous/notorious coaching inn(s)",
		"Foodstuffs",
		"Glass or pottery crafters",
		"Goats (meat, cheese and furs)",
		"Government (provincial court, office etc)"
		"Home of famous artist, actor or author",
		"Horse breeding",
		"Illicit services (strong thieves guild etc)",
		"Important agricultural producer",
		"Imposing bridge or other construction",
		"Impressive shrine, statue or memorial",
		"Impressive temple to major diety",
		"Inhabitants are ostracized by outsiders",
		"Known as a lawless place",
		"Large Dwarven community ({}%)".format(random.randint(1,10)*2),
		"Large library",
		"Large producer of charcoal",
		"Location makes settlement a natural fort",
		"Logging, timber and sawing",
		"Lush park, gardens or commons",
		"Major Road/River Warden station",
		"Mentioned in famous song, saga or poem",
		"Mighty watch tower or beacon",
		"Military strongpoint (double garrison)",
		"Mining (metal or mineral)",
		"Notorious for its corrupt officials",
		"On the decline (economically, politically)",
		"Part of the settlement is in ruins",
		"Preserves",
		"Recently under attack (by Greenskins etc)",
		"Rumoured to be a site of unnatural events",
		"Settlement has recently been prospering",
		"Settlement is geographically isolated",
		"Settlement of historical importance",
		"Sheep (meat, cheese and fur)",
		"Significant center of trade",
		"Significant fortification (25% of population are troops)",
		"Site of major prison or labour camp",
		"Site of recent unrest (riots, insurrections)",
		"Sizable Halfling community ({}%)".format(random.randint(1,10)*2),
		"Tradesmen are regarded as greedy",
		"Trapping (fur and skin)",
		"Wine (type depends on soil and tradition)"
	]

	Settlement_Purpose = [
	"Road/River convergance",
	"Road/River convergance",
	"Road/River convergance",
	"Natural resource",
	"Natural resource",
	"Natural resource",
	"Mining settlement",
	"Mining settlement",
	"Mining settlement",
	"Military/Strategic Value (Prior/Current staging point/important landmark)"
	]

	Trade_Resource = [
	"Grazing Land",
	"Grazing Land",
	"Grazing Land",
	"Grazing Land",
	"Flower Farms",
	"Flower Farms",
	"Grain Farms",
	"Grain Farms",
	"Natural Oils/Fuels",
	"Rare Animals"
	]

	Metal_Resouce = [
	"Copper",
	"Copper",
	"Tin",
	"Tin",
	"Iron",
	"Iron",
	"Silver",
	"Gold",
	"Exotic metal",
	"Special metal"
	]

	FBuildings = ['Farms']
	HBuildings = ['No Walls', 'Well', 'Longhouse', '2-3 Work houses', '>15 Hovels']
	VBuildings = ['Wooden Walls', '3 Wells', 'Manor House', 'Great Hall', 'Church', 'Blacksmith', 'Inn', '4-5 Work houses', '2-3 Shopfronts', '>30 Hovels', '>15 Homesteads']
	TBuildings = ['Stone Walls', 'Great Hall', '1-2 Church', '2-3 Blacksmiths', '2-3 Inns', '10 Work houses', '7-10 Shopfronts', 'Dedicated Market', '>100 Hovels', '>40 Homesteads']
	CBuildings = ['Towers', 'Sewers', '2-4 Government Buildings', '4+ Blacksmiths', '5+ Inns', '10+ Processing', '20+ Shopfronts', 'Dedicated Market', '3-4 Watch Barracks', '>200 Hovels', '>100 Homesteads', '>50 Manors']

	def create_name(self):
		first = random.choice(Settlement.First_Name)
		second = random.choice(Settlement.Second_Name)

		Settlement.filename = first+second

		Settlement.name = "Name: "+ first+second

	def create_size(self):
		population = random.randint(0, 4)
		people = random.randint(1, 10)

		if population == 0:
			#Farm
			Settlement.settlementType = "Type: "+Settlement.Settlement_Type[0]
			Settlement.population = "Population: "+str(random.randint(2,20))

		elif population == 1:
			#Hamlet
			Settlement.settlementType = "Type: "+Settlement.Settlement_Type[1]
			Settlement.population = "Population: "+str(people*10)

		elif population == 2:
			#Village
			Settlement.settlementType = "Type: "+Settlement.Settlement_Type[2]
			Settlement.population = "Population: "+str(people*100)

		elif population == 3:
			#Town
			Settlement.settlementType = "Type: "+Settlement.Settlement_Type[3]
			Settlement.population = "Population: "+str(people*1000)

		else:
			#City
			Settlement.settlementType = "Type: "+Settlement.Settlement_Type[4]
			Settlement.population = "Population: "+str(people*500+10000)

	def create_features(self):
		Settlement.features = "Notable Features: {}".format(random.choice(Settlement.Settlement_Features))

	def create_buildings(self):
		if Settlement.settlementType == 'Type: Farm':
			Settlement.buildings = Settlement.FBuildings
		elif Settlement.settlementType == 'Type: Hamlet':
			Settlement.buildings = Settlement.HBuildings
		elif Settlement.settlementType == 'Type: Village':
			Settlement.buildings = Settlement.VBuildings
		elif Settlement.settlementType == 'Type: Town':
			Settlement.buildings = Settlement.TBuildings
		else:
			Settlement.buildings = Settlement.CBuildings
	def create_purpose(self):
		var = random.randint(0, 10)

		if var <= 2:
			#Road/River Convergence
			Settlement.purpose = "Purpose: Road/River Convergence"
			Settlement.resources = "Resources: "+random.choice(Settlement.Trade_Resource)

		elif 3 <= var <= 5:
			#Natural Resource
			Settlement.purpose = "Purpose: Natural Resources"
			temp1 = random.choice(Settlement.Trade_Resource)
			temp2 = random.choice(Settlement.Trade_Resource)

			if temp1 == temp2:
				Settlement.resources = "Resources: "+temp1+". This land is doubly fertile and has a 50% chance to have rare or legendary crops/creatures/fuels."
			else:
				Settlement.resources = "Resources: "+temp1+" and "+temp2


		elif var == 6 or var == 7:
			#Mining Settlement
			Settlement.purpose = "Purpose: Mining Settlement"
			Settlement.resources = "Resources: "+random.choice(Settlement.Metal_Resouce)+" and "+random.choice(Settlement.Trade_Resource)

		else:
			#Military/Strategic Value
			Settlement.purpose = "Purpose: Military/Strategic Value"
			Settlement.resources = "Resources: "+random.choice(Settlement.Metal_Resouce)


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

	file.write(MySettlements[x].purpose + '\n')

	file.write(MySettlements[x].features + '\n')

	file.write(MySettlements[x].resources + '\n')

	file.write("Buildings: " + '\n')
	for elem in MySettlements[x].buildings:
		file.write(elem + '\n')

	file.write("Notes: \n")

	file.close()
