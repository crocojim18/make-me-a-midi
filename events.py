from functions import *

class Event:
	def __init__(self):
		self.deltaTime = 0

	def setDelta(self, delta):
		self.deltaTime = int2vl(delta)

### Meta events ###

class TempoEvent(Event):
	def __init__(self, deltaTime=0, tempo=500000):
		self.deltaTime = deltaTime
		self.header = bytearray([0xFF,0x51,3])
		self.time = tempo
		
	def setTempo(self, time):
		if 0 <= time <= 0xffffff:
			self.time = time
		else:
			print "Tempo of {} not set.".format(time)
			
	def __str__(self):
		toReturn = int2vl(self.deltaTime)
		toReturn += self.header
		toReturn += int2bin(self.time, 3)
		return toReturn
		
class EndOfTrackEvent(Event):
	def __init__(self, deltaTime=0):
		self.deltaTime = deltaTime
		self.header = bytearray([0xFF,0x2F,0x00])
		
	def __str__(self):
		toReturn = int2vl(self.deltaTime)
		toReturn += self.header
		return toReturn