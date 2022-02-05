from time import perf_counter, sleep
from art import tprint
from random import choice, randint
from os import name, system
from compress_json import local_load, local_dump

class Kyper:
	def __init__(self, xtype=1, uname="guest", length=16, website="google.com", allowed={"spec":False,"nums":True,"letr":True,"genrc":True}):
		self.name = "Kyper"
		self.version = "0.0.1"
		self.os = name
		self.path = "./db/stores.lzma"

		self.colours = {
			"reverse" : str("\033[;7m"),
			"green" : str("\033[0;32m"),
			"blue" : str("\033[1;34m"),
			"cyan" : str("\033[1;36m"),
			"reset" : str("\033[0;0m"),
			"yellow" : str("\033[33m"),
			"header" : str("\033[95m"),
			"red" : str("\033[1;31m"),
			"bold" : str("\033[;1m")
		}

		self.placeholders = [
			"pAsWordD",
			"PAOSPwORD",
			"whatIsThis",
			"whenDoWeStart",
			"FarFromHome",
			"WeEatNo",
			"MyCronJObDied",
			"WhatIsLinux",
			"HowToPython"
		]

		self.symbols = {
			"spec": "éúíóáę€ółśążźćń$αβγδεζηϑθικλμν`ξοπϖρσςτυφχψω∼≈≅≡≠±√⋅×∗÷¼½¾∝∞ƒ∫∂∠⊥°′″⊕⊗∇⋅×∧∨∴",
			"nums": "1234567890",
			"letr": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
			"genrc": "!£$%^&*()_+=-[]}{;'#~@:/.,<>?'"
		}

		self.errprfx = f"{self.colours['red']}KError{self.colours['cyan']}:{self.colours['yellow']}"

		self.type = xtype
		self.uname = uname
		self.length = length
		self.website = website
		self.allowed = allowed

	def clear(self, title=True):
		if self.os == 'nt': 
			_ = system('cls')
			
		else: 
			_ = system('clear')

	def title(self, text="Kyper", colour="yellow"):
		try:
			print(self.colours[colour])
			tprint(text)
			print(self.colours['reset'])
		except:
			print(f"{self.errprfx} no colour \"{colour}\" in colour list.{self.colours['reset']}")

	def write_pwd(self, data): local_dump(data, self.path)
	def read_pwd(self): return local_load(self.path)

	def handle(self):
		if self.type == 1:

			val = local_load(self.path)
			
			b = 1
			for i in val:
				print(f"\n{self.colours['green']}[{b}] {self.colours['cyan']}Website: {i}\n\tUsername: {self.colours['yellow']}{val[i][0]}\n\t{self.colours['cyan']}Password: {self.colours['yellow']}{val[i][1]}\n{self.colours['reset']}")

			return 0

		elif self.type == 2:
			kyper.generate()

		elif self.type == 3:
			try:
				backup = local_load(self.path)
				backup.pop(self.website)
				kyper.write_pwd(backup)
			except EOFError:
				print(f"{self.errprfx} Incomplete {self.path} lzma file.{colours['reset']}")

		else:
			print(f"{self.errprfx} Unknown type \"{self.type}\".{colours['reset']}")

	def generate(self, generated=[]):

		rnd = kyper.randomizer()
		self.generated = generated

		i = 0
		while i < int(len(rnd)*1.5):
			rnd[choice(range(len(rnd)))] = choice(range(len(rnd)))
			i += 1

		while len(self.generated) != self.length:
			try:
				self.generated.append(rnd[choice(range(len(rnd)))])
			except TypeError:
				self.generated.append(rnd[choice(range(len(rnd)))])

		b = 0
		for i in self.generated:
			try:
				if i > 100:
					i /= 100
					i = int(i)
				elif i > 10:
					i /= 10
					i = int(i)
				else:
					i *= choice(self.symbols['letr'])

				self.generated[b] = i

			except TypeError:
				pass

			b += 1

		try:
			backup = local_load(self.path)
		except EOFError:
			backup = {}

		backup[self.website] = [self.uname, ''.join(str(i) for i in self.generated)] 
		kyper.write_pwd(backup)

		return self.generated

	def randomizer(self):

		placeholders = list(choice(self.placeholders))

		if self.allowed['spec']:
			for i in range(int(((5+(int(len(range(len(placeholders))))*2)/self.length)*(self.length/2.5))+int(perf_counter()))):
				placeholders.append(choice(self.symbols["spec"]))

		if self.allowed['nums']:
			for i in range(int(((4+(int(len(range(len(placeholders))))*3)/self.length)*(self.length/2.6))+int(perf_counter()))):
				placeholders.append(choice(self.symbols["nums"]))
			
		if self.allowed['letr']:
			for i in range(int(((3+(int(len(range(len(placeholders))))*4)/self.length)*(self.length/2.7))+int(perf_counter()))):
				placeholders.append(choice(self.symbols["letr"]))

		if self.allowed['genrc']:
			for i in range(int(((2+(int(len(range(len(placeholders))))*5)/self.length)*(self.length/2.8))+int(perf_counter()))):
				placeholders.append(choice(self.symbols["genrc"]))

		self.randomized = placeholders

		return self.randomized

if __name__ == '__main__':

	debug = False

	kyper = Kyper()
	kyper.clear()
	kyper.title()

	if debug:
		print(local_load("./db/stores.lzma"))
		kyper.handle()

	else:
		arq = input(f"{kyper.colours['reset']}Do you want to list, add or remove a password? {kyper.colours['bold']}> ")

		if arq == "list":
			kyper.handle()

		elif arq == "add":

			nq = input(f"{kyper.colours['reset']}What do you want your username/email to be? {kyper.colours['bold']}> ")
			webq = input(f"{kyper.colours['reset']}What website do you want to {arq}? {kyper.colours['bold']}> ")
			lenq = input(f"{kyper.colours['reset']}What is your preferred length for the password? {kyper.colours['bold']}> ")
			symbq = input(f"{kyper.colours['reset']}Which features would you like in your password;\n\t{kyper.colours['cyan']}-{kyper.colours['reset']} Special Characters\n\t{kyper.colours['cyan']}-{kyper.colours['reset']} Numbers\n\t{kyper.colours['cyan']}-{kyper.colours['reset']} Letters\n\t{kyper.colours['cyan']}-{kyper.colours['reset']} Generic Symbols\n\n\t{kyper.colours['cyan']}Keep in mind: write your answer in order:\n\tfor example, {kyper.colours['yellow']}Y/N/N/Y{kyper.colours['cyan']}, would be Yes to special\n\tcharacters and generic symbols, but no to\n\tletters and numbers.\n\n\t{kyper.colours['bold']}> ")
			symbq = symbq.split("/")

			kyper = Kyper(2, nq, int(lenq), webq, {"spec": True if symbq[0].upper() == "Y" else False, "nums": True if symbq[1].upper() == "Y" else False, "letr": True if symbq[2].upper() == "Y" else False, "genrc": True if symbq[3].upper() == "Y" else False})
			kyper.handle()
		
		elif arq == "remove":
			nq = input(f"{kyper.colours['reset']}What website do you want to remove? {kyper.colours['bold']}> ")

			kyper = Kyper(3, webq)
			kyper.handle()