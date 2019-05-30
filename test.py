from midiFunctions import *
from events import *
from structures import *
from musicFunctions import *

work = open("out.mid", 'wb')

head = Header()

cof = COF()
print "cb major: "+str(cof.getScale("cb", "maj"))
print "b major: "+str(cof.getScale("b", "maj"))

tra = Track()
tra.addEvent(TimeSignatureEvent(num=4, denom=4))
tra.addEvent(TempoEvent(tempo=140))
tra.addEvent(TrackNameEvent(name="Tempo Track"))
tra.addEvent(ProgramChangeEvent(instrument=12))
tra.addEvent(EndOfTrackEvent(deltaTime=7680))

tra2 = Track()
tra2.addEvent(TrackNameEvent(name="Arpeggio Down"))

total = 7680
noteState = 0
measureState = 0
note = "c5"
while total > 7680-(96*8*4):
	if measureState == 0:
		if noteState in [0,3,6]:
			note = "c5"
		elif noteState in [1,4,7]:
			note = "a4"
		elif noteState in [2,5]:
			note = "f4"
	elif measureState == 1:
		if noteState in [0,3,6]:
			note = "f4"
		elif noteState in [1,4,7]:
			note = "d4"
		elif noteState in [2,5]:
			note = "bb3"
	elif measureState == 2:
		if noteState in [0,3,6]:
			note = "a4"
		elif noteState in [1,4,7]:
			note = "f4"
		elif noteState in [2,5]:
			note = "d4"
	elif measureState == 3:
		if noteState in [0,3,6]:
			note = "g4"
		elif noteState in [1,4,7]:
			note = "e4"
		elif noteState in [2,5]:
			note = "c4"
	tra2.addEvent(NoteOnEvent(note=note2int(note), velocity=100))
	tra2.addEvent(NoteOffEvent(deltaTime=96, note=note2int(note), velocity=0))
	if noteState == 7:
		noteState = 0
		if measureState <= 3:
			measureState += 1
		else:
			measureState = 0
	else:
		noteState += 1
	total -= 96

tra2.addEvent(EndOfTrackEvent(deltaTime=total))

head.addTrack(tra)
head.addTrack(tra2)

work.write(head.__str__())
work.close()