from midiFunctions import *

class Header:
	def __init__(self, format=1, division=192):
		self.magicNumber = "MThd"
		self.length = 6
		self.format = format
		self.tracks = []
		self.numOfTracks = len(self.tracks)
		self.division = division
		
	def addTrack(self, track):
		self.tracks.append(track)
		self.numOfTracks = len(self.tracks)

	def setDivision(self, division):
		self.division = division

	def __str__(self):
		toReturn = self.magicNumber + int2bin(self.length,4) 
		toReturn += int2bin(self.format, 2)
		toReturn += int2bin(self.numOfTracks, 2)
		toReturn += int2bin(self.division, 2)
		for i in self.tracks:
			toReturn += i.__str__()
		return toReturn
		
class Track:
	def __init__(self):
		self.magicNumber = "MTrk"
		self.length = 0
		self.events = []
		
	def addEvent(self, event):
		self.events.append(event)
		self.length += len(event.__str__())
		
	def __str__(self):
		toReturn = self.magicNumber
		toReturn += int2bin(self.length, 4)
		for i in self.events:
			toReturn += i.__str__()
		return toReturn