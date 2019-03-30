''' NIM/Nama  : 13517065/Andrian Cedric, 13517137/Vincent Budianto
	Nama file : MazeEscape.py
	Topik     : Tugas Kecil III IF2211-Strategi Algoritma
	Tanggal   : 01 April 2019
	Deskripsi : Source code  menggunakan strategi algoritma BFS dan A* '''

from colorama import *
from time import *
import os
import queue

#inisialisasi variabel global
global filename
global defaultMaps
global maps
global startPos
global endPos
global path
global liveNode
global deadNode
global inputMenu

class Node():
	#Ctor
	def __init__(self, prev=None, pos=None):
		self.prev = prev
		self.pos = pos
		self.f = 0

#inisialisasi variabel
startPos = Node(None, None)
endPos = Node(None, None)
path = []
liveNode = []
deadNode = []

def start():
	#Kamus
	global startPos

	#Algoritma
	for i in range(len(maps)):
		if (maps[i][0] == 0):
			s = (i, 0)
	
	startPos = Node(None, s)
	startPos.f = heu(startPos)

def end():
	#Kamus
	global endPos
	
	#Algoritma
	for i in range(len(maps)):
		if (maps[i][len(maps[i]) - 1] == 0):
			e = (i, len(maps[i]) - 1)

	endPos = Node(None, e)
	endPos.f = heu(endPos)

def heu(x):
	#Algoritma
	a = endPos.pos[0] - x.pos[0]
	b = endPos.pos[1] - x.pos[1]

	return abs(a + b)
	
def load():
	#Kamus
	global filename
	global defaultMaps
	global maps
	
	#Algoritma
	if (not('.txt' in filename)):
		filename += '.txt'
	
	F = open(filename, 'r').read().split('\n')
	a = len(F)
	b = len(F[0])
	maps = [[0 for x in range (a)] for y in range(b)]
	defaultMaps = [[0 for x in range (a)] for y in range(b)]
	
	for i in range(len(F)):
		for j in range(len(F[i])):
			if (F[i][j] == '1'):
				maps[i][j] = 1
				defaultMaps[i][j] = 1
			else:
				maps[i][j] = 0
				defaultMaps[i][j] = 0
	
	end()
	start()

def aStar():
	#Kamus
	global maps
	global path
	global liveNode
	global deadNode

	#Algoritma
	curr = startPos
	liveNode.append(curr)

	while liveNode:
		adj = []
		curr = min(liveNode, key = lambda n:n.f)
	
		if ((curr.pos[0] == endPos.pos[0]) and (curr.pos[1] == endPos.pos[1])):
			while curr.prev:
				path.append(curr)
				curr = curr.prev
			
			path.append(curr)
			
			for i in range(len(path)):
				maps[path[i].pos[0]][path[i].pos[1]] = 2
			
			break
		
		liveNode.remove(curr)
		deadNode.append(curr)
		
		for i in range(len(deadNode)):
			maps[deadNode[i].pos[0]][deadNode[i].pos[1]] = 3
				
		for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			nextNode = (curr.pos[0] + move[0], curr.pos[1] + move[1])
			
			if ((nextNode[0] > (len(maps) - 1)) or (nextNode[0] < 0) or (nextNode[1] > (len(maps[len(maps)-1]) -1)) or (nextNode[1] < 0)):
				continue

			if (maps[nextNode[0]][nextNode[1]] != 0):
				continue
			
			if ((nextNode[0] == curr.pos[0]) and (nextNode[1] == curr.pos[1])):
				continue
			
			newNode = Node(curr, nextNode)
			adj.append(newNode)

		for i in adj:
			for j in deadNode:
				if (i == j):
					continue
			
			i.f = curr.f - heu(curr) + heu(i) + 1 
			
			for j in liveNode:
				if ((i == j) and (i.f > j.f)):
					continue
			
			liveNode.append(i)

def BFS():
	#Kamus
	global maps
	global path
	global liveNode
	global deadNode

	#Algoritma
	curr = startPos
	liveNode.append(curr)

	while liveNode:
		adj = []
		curr = min(liveNode, key = lambda n:n.f)
		if ((curr.pos[0] == endPos.pos[0]) and (curr.pos[1] == endPos.pos[1])):
			while curr.prev:
				path.append(curr)
				curr = curr.prev
			path.append(curr)
			for i in range(len(path)):
				maps[path[i].pos[0]][path[i].pos[1]] = 2
			
			break
			
		liveNode.remove(curr)
		deadNode.append(curr)
		
		for i in range(len(deadNode)):
			maps[deadNode[i].pos[0]][deadNode[i].pos[1]] = 3
				
		for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			nextNode = (curr.pos[0] + move[0], curr.pos[1] + move[1])
			
			if ((nextNode[0] > (len(maps) - 1)) or (nextNode[0] < 0) or (nextNode[1] > (len(maps[len(maps)-1]) -1)) or (nextNode[1] < 0)):
				continue

			if (maps[nextNode[0]][nextNode[1]] != 0):
				continue
			
			if ((nextNode[0] == curr.pos[0]) and (nextNode[1] == curr.pos[1])):
				continue
			
			newNode = Node(curr, nextNode)
			adj.append(newNode)

		for i in adj:
			for j in deadNode:
				if (i == j):
					continue
			
			i.f = curr.f + 1 
			
			for j in liveNode:
				if ((i == j)and (i.f > j.f)):
					continue
			
			liveNode.append(i)

def printMaze():
	#Kamus
	global maps
	
	#Algoritma
	print(Style.BRIGHT + 'Maze :')
	print(end = ' ')
	
	for x in range(len(maps[len(maps) - 1]) + 4):
		print(Style.BRIGHT + Back.WHITE + ' ', end = '')

	print()
	
	for i in range(len(maps)):
		print(' ', end = '')
		print(Style.BRIGHT + Back.WHITE + '  ', end = '')
		
		for j in range(len(maps[i])):
			if ((i == startPos.pos[0]) and (j == startPos.pos[1])):
				print(Style.BRIGHT + Back.CYAN + ' ', end = '')
			elif ((i == endPos.pos[0]) and (j == endPos.pos[1])):
				print(Style.BRIGHT + Back.CYAN + ' ', end = '')
			elif (maps[i][j] == 1):
				print(Style.BRIGHT + Back.BLACK + ' ', end = '')
			elif (maps[i][j] == 0):
				print(Style.BRIGHT + Back.WHITE + ' ', end = '')
			
			if (j == (len(maps[i]) - 1)):
				print(Style.BRIGHT + Back.WHITE + '  ')

	print(' ', end = '')

	for x in range(len(maps[len(maps) - 1]) + 4):
		print(Style.BRIGHT + Back.WHITE + ' ', end = '')

	print()

def printResult():
	#Kamus
	global maps
	
	#Algoritma
	print(Style.BRIGHT + 'Result:')
	print(end = ' ')
	
	for x in range(len(maps[len(maps) - 1]) + 4):
		print(Style.BRIGHT + Back.WHITE + ' ', end = '')

	print()
	
	for i in range(len(maps)):
		print(' ', end = '')
		print(Style.BRIGHT + Back.WHITE + '  ', end = '')
		
		for j in range(len(maps[i])):
			if (maps[i][j] == 3):
				print(Style.BRIGHT + Back.RED + ' ', end = '')
			elif (maps[i][j] == 2):
				print(Style.BRIGHT + Back.GREEN + ' ', end = '')
			elif (maps[i][j] == 1):
				print(Style.BRIGHT + Back.BLACK + ' ', end = '')
			elif (maps[i][j] == 0):
				print(Style.BRIGHT + Back.WHITE + ' ', end = '')
			
			if (j == (len(maps[i]) - 1)):
				print(Style.BRIGHT + Back.WHITE + '  ')

	print(' ', end = '')

	for x in range(len(maps[len(maps) - 1]) + 4):
		print(Style.BRIGHT + Back.WHITE + ' ', end = '')
	
	print()

def reset():
	#Kamus
	global maps
	global path
	global liveNode
	global deadNode
	
	#Algoritma
	path.clear()
	liveNode.clear()
	deadNode.clear()
	
	for i in range(len(maps)):
		for j in range(len(maps[i])):
			maps[i][j] = defaultMaps[i][j]

#Program Utama
init(autoreset=True)
inputMenu = 0
valid = False

while (not valid):
	try:
		os.system('cls')

		print(Style.BRIGHT + Fore.MAGENTA + '________________________________________________________________________\n|  ', end = '')
		print(Style.BRIGHT + Fore.CYAN + ' __  __                     ______                               ', end = '')
		print(Style.BRIGHT + Fore.MAGENTA + '   |\n|  ', end = '')
		print(Style.BRIGHT + Fore.CYAN + '|  \\/  |                   |  ____|                              ', end = '')
		print(Style.BRIGHT + Fore.MAGENTA + '   |\n|  ', end = '')
		print(Style.BRIGHT + Fore.CYAN + '| \\  / |  __ _  ____  ___  | |__    ___   ___   __ _  _ __    ___ ', end = '')
		print(Style.BRIGHT + Fore.MAGENTA + '  |\n|  ', end = '')
		print(Style.BRIGHT + Fore.CYAN + '| |\\/| | / _` ||_  / / _ \ |  __|  / __| / __| / _` || \'_ \\  / _ \\', end = '')
		print(Style.BRIGHT + Fore.MAGENTA + '  |\n|  ', end = '')
		print(Style.BRIGHT + Fore.CYAN + '| |  | || (_| | / / |  __/ | |____ \\__ \\| (__ | (_| || |_) ||  __/', end = '')
		print(Style.BRIGHT + Fore.MAGENTA + '  |\n|  ', end = '')
		print(Style.BRIGHT + Fore.CYAN + '|_|  |_| \\__,_|/___| \\___| |______||___/ \\___| \\__,_|| .__/  \\___|', end = '')
		print(Style.BRIGHT + Fore.MAGENTA + '  |\n|  ', end = '')
		print(Style.BRIGHT + Fore.CYAN + '                                                     | |          ', end = '')
		print(Style.BRIGHT + Fore.MAGENTA + '  |\n|  ', end = '')
		print(Style.BRIGHT + Fore.CYAN + '                                                     |_|          ', end = '')
		print(Style.BRIGHT + Fore.MAGENTA + '  |')
		print(Style.BRIGHT + Fore.MAGENTA + '|______________________________________________________________________|\n')

		filename = input(Style.BRIGHT + Fore.YELLOW + 'Masukan nama file : ')
		load()
		valid = True
	except:
		print(Style.BRIGHT + Fore.RED + filename + ' Not Found')
		sleep(1)

while (inputMenu != 4):
	os.system('cls')
	valid = False
	printMaze()
	
	while (not valid):
		try:
			print()
			print(Style.BRIGHT + 'Menu :')
			print(Style.BRIGHT + '1. Algoritma BFS')
			print(Style.BRIGHT + '2. Algoritma A*')
			print(Style.BRIGHT + '3. Change File')
			print(Style.BRIGHT + '4. Exit')
			inputMenu = input(Style.BRIGHT + Fore.CYAN + '\nMasukan jenis algoritma: ')		
			valid = True
		except IOError:
			print(Style.BRIGHT + Fore.RED + 'Invalid input.')
			sleep(1)

	if (inputMenu == '1'):
		BFS()
		os.system('cls')
		printResult()
		reset()
		input(Style.BRIGHT + Fore.BLUE + '\n--- CONTINUE ---')
	elif (inputMenu == '2'):
		aStar()
		os.system('cls')
		printResult()
		reset()
		input(Style.BRIGHT + Fore.BLUE + '\n--- CONTINUE ---')
	elif (inputMenu == '3'):
		try:
			filename = input(Style.BRIGHT + Fore.YELLOW + '\nMasukan nama file : ')
			load()
			valid = True
		except:
			print(Style.BRIGHT + Fore.RED + filename + ' Not Found')
			sleep(0.8)
	elif (inputMenu == '4'):
		exit()
