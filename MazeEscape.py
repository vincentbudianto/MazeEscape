''' NIM/Nama  : 13517065/Andrian Cedric, 13517137/Vincent Budianto
	Nama file : MazeEscape.py
	Topik     : Tugas Kecil III IF2211-Strategi Algoritma
	Tanggal   : 01 April 2019
	Deskripsi : Source code  menggunakan strategi algoritma BFS dan A* '''

from colorama import *
import queue

#inisialisasi variabel global
global maps
global startpos
global endpos
global queue1
global queue2

#inisialisasi variabel
startpos = ()
endpos = ()
#queue1 = queue.Queue()
queue2 = queue.PriorityQueue()

def start():
	global maps
	global startpos

	for i in range(len(maps)):
		if (maps[i][0] == 0):
			startpos = (0, i)

def end():
	global maps
	global endpos
	
	for i in range(len(maps)):
		if (maps[i][len(maps[i]) - 1] == 0):
			endpos = (len(maps[i]) - 1, i)

def load():
	global maps
	
	F = open('test2.txt', 'r').read().split('\n')
	a = len(F)
	b = len(F[0])
	maps = [[0 for x in range (a)] for y in range(b)]
	
	for i in range(len(F)):
		for j in range(len(F[i])):
			if (F[i][j] == '1'):
				maps[i][j] = 1
			else:
				maps[i][j] = 0
	
	start()
	end()

def heu(x, y):
	a = endpos[0] - x
	b = endpos[0] - y
	heuristic = a + b

	return abs(heuristic)

def Astar(x, y):
	global queue2
	
	if ((x == endpos[0]) and (y == endpos[0])):
		print('A* path :')
	else:
		queue2.put((heu(x, y), (x, y)))
	
def printMaze():
	global maps
	
	print(end = ' ')
	
	for x in range(len(maps[len(maps) - 1]) + 4):
		print(Back.WHITE + ' ', end = '')

	print()
	
	for i in range(len(maps)):
		print(' ', end = '')
		print(Back.WHITE + '  ', end = '')
		for j in range(len(maps[i])):
			if (maps[i][j] == 1):
				print(Back.BLACK + ' ', end = '')
			elif (maps[i][j] == 0):
				print(Back.WHITE + ' ', end = '')
			
			if (j == (len(maps[i]) - 1)):
				print(Back.WHITE + '  ')

	print(' ', end = '')

	for x in range(len(maps[len(maps) - 1]) + 4):
		print(Back.WHITE + ' ', end = '')

	print()


def printResult():
	global maps
	
	print(end = ' ')
	
	for x in range(len(maps[len(maps) - 1]) + 4):
		print(Back.WHITE + ' ', end = '')

	print()
	
	for i in range(len(maps)):
		print(' ', end = '')
		print(Back.WHITE + '  ', end = '')
		for j in range(len(maps[i])):
			if (maps[i][j] == 2):
				print(Back.GREEN + ' ', end = '')
			elif (maps[i][j] == 1):
				print(Back.BLACK + ' ', end = '')
			elif (maps[i][j] == 0):
				print(Back.WHITE + ' ', end = '')
			
			if (j == (len(maps[i]) - 1)):
				print(Back.WHITE + '  ')

	print(' ', end = '')

	for x in range(len(maps[len(maps) - 1]) + 4):
		print(Back.WHITE + ' ', end = '')
	
	print()


init(autoreset=True)
load()
printMaze()
print(startpos)
print(endpos)
