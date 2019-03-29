''' NIM/Nama  : 13517065/Andrian Cedric, 13517137/Vincent Budianto
	Nama file : Node.py
	Topik     : Tugas Kecil III IF2211-Strategi Algoritma
	Tanggal   : 01 April 2019
	Deskripsi : Class Node untuk A* '''

class Node():
	def __init__(self, prev=None, pos=None):
		self.prev = prev
		self.pos = pos
		self.f = 0
