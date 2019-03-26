''' NIM/Nama  : 13517065/Andrian Cedric, 13517137/Vincent Budianto
	Nama file : file.py
	Topik     : Tugas Kecil III IF2211-Strategi Algoritma
	Tanggal   : 13 Februari 2019
	Deskripsi : Implementasi untuk fungsi file eksternal '''

#inisialisasi variabel global
global maps
global startpos
global endpos

#inisialisasi variabel
maps = []
startpos = {'x': '', 'y': ''}
endpos = {'x': '', 'y': ''}

def start():
	global maps
	global startpos

	for i in range(len(maps)):
		if (maps[i][0] == '0'):
			startpos['x'] = 0
			startpos['y'] = i

def end():
	global maps
	global endpos
	
	for i in range(len(maps)):
		if (maps[i][len(maps[i]) - 1] == '0'):
			endpos['x'] = len(maps[i]) - 1
			endpos['y'] = i

def load():
	global maps
	
	maps = open('test1.txt', 'r').read().split('\n')
	
	start()
	end()

''' Driver:
print('maps :', maps)
print('startpos :', startpos)
print('endpos :', endpos)
load()
print('maps :', maps)
print('startpos :', startpos)
print('endpos :', endpos)
'''
