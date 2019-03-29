''' NIM/Nama  : 13517065/Andrian Cedric, 13517137/Vincent Budianto
	Nama file : File.py
	Topik     : Tugas Kecil III IF2211-Strategi Algoritma
	Tanggal   : 13 Februari 2019
	Deskripsi : Implementasi untuk fungsi file eksternal '''

from colorama import *

#inisialisasi variabel global
global maps
global startpos
global endpos

#inisialisasi variabel
startpos = {'x': '', 'y': ''}
endpos = {'x': '', 'y': ''}

def start():
	global maps
	global startpos

	for i in range(len(maps)):
		if (maps[i][0] == 0):
			startpos['x'] = 0
			startpos['y'] = i

def end():
	global maps
	global endpos
	
	for i in range(len(maps)):
		if (maps[i][len(maps[i]) - 1] == 0):
			endpos['x'] = len(maps[i]) - 1
			endpos['y'] = i

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

''' Driver:
print('maps :')
for i in range(len(maps)):
	print(i, ': ', end = '')
	print(maps[i])
print('startpos :', startpos)
print('endpos :', endpos)
'''
'''
for i in range(len(maps)):
	print(i, ': ', end = '')
	print(maps[i])

maps[0][0] = 0
print('\nubah maps[0][0] dari 1 ke 0\n')

for i in range(len(maps)):
	print(i, ': ', end = '')
	print(maps[i])
'''

init(autoreset=True)
load()
print('startpos :', str(startpos['x']) + ', ' + str(startpos['y']))
print('endpos   :', str(endpos['x']) + ', ' + str(endpos['y']))
print('Maze :')
print(' ', end = '')

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
