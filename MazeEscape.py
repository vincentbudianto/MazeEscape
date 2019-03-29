''' NIM/Nama  : 13517065/Andrian Cedric, 13517137/Vincent Budianto
	Nama file : MazeEscape.py
	Topik     : Tugas Kecil III IF2211-Strategi Algoritma
	Tanggal   : 01 April 2019
	Deskripsi : Source code  menggunakan strategi algoritma BFS dan A* '''

from Node import *
from colorama import *
import queue

#inisialisasi variabel global
global maps
global startPos
global endPos
global path
global openNode
global closedNode

#inisialisasi variabel
startPos = Node(None, None)
endPos = Node(None, None)
path = []
openNode = []
closedNode = []

def start():
	global startPos

	for i in range(len(maps)):
		if (maps[i][0] == 0):
			s = (i, 0)
	
	startPos = Node(None, s)
	startPos.f = heu(startPos)

def end():
	global endPos
	
	for i in range(len(maps)):
		if (maps[i][len(maps[i]) - 1] == 0):
			e = (i, len(maps[i]) - 1)

	endPos = Node(None, e)
	endPos.f = heu(endPos)
	
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
	
	end()
	start()

def heu(x):
	a = endPos.pos[0] - x.pos[0]
	b = endPos.pos[1] - x.pos[1]

	return abs(a + b)

def aStar():
	global maps
	global path
	global openNode
	global closedNode

	curr = startPos
	openNode.append(curr)

	while openNode:
		adj = []
		curr = min(openNode, key = lambda n:n.f)
	
		if ((curr.pos[0] == endPos.pos[0]) and (curr.pos[1] == endPos.pos[1])):
			while curr.prev:
				path.append(curr)
				curr = curr.prev
			
			path.append(curr)
			
			for i in range(len(path)):
				maps[path[i].pos[0]][path[i].pos[1]] = 2
			
			break
		
		openNode.remove(curr)
		closedNode.append(curr)
		
		for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			nextNode = (curr.pos[0] + move[0], curr.pos[1] + move[1])
			
			if ((nextNode[0] > (len(maps) - 1)) or (nextNode[0] < 0) or (nextNode[1] > (len(maps[len(maps)-1]) -1)) or (nextNode[1] < 0)):
				continue

			if ((maps[nextNode[0]][nextNode[1]]) != 0):
				continue
			
			if ((nextNode[0] == curr.pos[0]) and (nextNode[1] == curr.pos[1])):
				continue
			
			newNode = Node(curr, nextNode)
			adj.append(newNode)
		
		for i in range(len(adj)):
			maps[adj[i].pos[0]][adj[i].pos[1]] = 3
		
		for i in adj:
			for j in closedNode:
				if (i == j):
					continue
			
			i.f = curr.f - heu(curr) + heu(i) + 1 
			
			for j in openNode:
				if ((i == j) and (i.f > j.f)):
					continue
			
			openNode.append(i)

def printMaze():
	global maps
	
	print('Maze :')
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
	
	print('A* Result:')
	print(end = ' ')
	
	for x in range(len(maps[len(maps) - 1]) + 4):
		print(Back.WHITE + ' ', end = '')

	print()
	
	for i in range(len(maps)):
		print(' ', end = '')
		print(Back.WHITE + '  ', end = '')
		
		for j in range(len(maps[i])):
			if (maps[i][j] == 3):
				print(Back.RED + ' ', end = '')
			elif (maps[i][j] == 2):
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

for i in range(len(maps)):
	print(i, end = ': ')
	print(maps[i])

print('start :', startPos.pos)
print('end   :',endPos.pos)
printMaze()
aStar()
printResult()
