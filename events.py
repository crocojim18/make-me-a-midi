from functions import *
from math import log

class Event:
	def __init__(self):
		self.deltaTime = 0

	def setDelta(self, delta):
		self.deltaTime = int2vl(delta)

### Voice events ###

class NoteEvent(Event):
	def __init__(self, deltaTime = 0, channel=1, note=0x3c, velocity=0x40):
		self.deltaTime = deltaTime
		self.channel = channel
		self.note = note
		self.velocity = velocity
		
	def setNote(self, note):
		self.note = note
		
	def setVelocity(self, velocity):
		self.velocity = velocity
		
	def setChannel(self, channel):
		self.channel = channel
		
class NoteOffEvent(NoteEvent):
	def __str__(self):
		if self.channel > 16:
			print "Invalid channel. Channel is greater than 16."
			return
		toReturn = int2vl(self.deltaTime)
		toReturn += int2bin(0x80+(self.channel-1),1)
		toReturn += int2bin(self.note,1)
		toReturn += int2bin(self.velocity,1)
		return toReturn
		
class NoteOnEvent(NoteEvent):
	def __str__(self):
		if self.channel > 16:
			print "Invalid channel. Channel is greater than 16."
			return
		toReturn = int2vl(self.deltaTime)
		toReturn += int2bin(0x90+(self.channel-1),1)
		toReturn += int2bin(self.note,1)
		toReturn += int2bin(self.velocity,1)
		return toReturn

### Meta events ###
		
class EndOfTrackEvent(Event):
	def __init__(self, deltaTime=0):
		self.deltaTime = deltaTime
		self.header = bytearray([0xFF,0x2F,0x00])
		
	def __str__(self):
		toReturn = int2vl(self.deltaTime)
		toReturn += self.header
		return toReturn
		
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

#todo: add clock functionality
class TimeSignatureEvent(Event):
	def __init__(self, deltaTime=0, num=4, denom=4, clocks=24, notes32=8):
		self.deltaTime = deltaTime
		self.header = bytearray([0xff, 0x58, 0x04])
		self.num = num
		self.denom = denom
		self.clocks = clocks
		self.notes32 = notes32
		
	def setTimeSignature(self, num, denom):
		self.num = num
		self.denom = denom
		
	def __str__(self):
		toReturn = int2vl(self.deltaTime) + self.header
		toReturn += int2bin(self.num, 1)
		toReturn += int2bin(int(log(self.denom, 2)), 1)
		toReturn += int2bin(self.clocks, 1)
		toReturn += int2bin(self.notes32, 1)
		return toReturn
		
class TrackNameEvent(Event):
	def __init__(self, deltaTime=0, name="New Track"):
		self.deltaTime = deltaTime
		self.header = bytearray([0xff, 3])
		self.name = name
		self.length = len(self.name)
		
	def setName(self, name):
		self.name = name
		self.length = len(self.name)
		
	def __str__(self):
		toReturn = int2vl(self.deltaTime)
		toReturn += self.header
		toReturn += int2vl(self.length)
		toReturn += self.name
		return toReturn
		