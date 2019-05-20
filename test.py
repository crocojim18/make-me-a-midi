from functions import *
from events import *
from structures import *

work = open("out.mid", 'wb')

head = Header()

tra = Track()
tra.addEvent(TimeSignatureEvent(num=4, denom=4))
tra.addEvent(TempoEvent())
tra.addEvent(TrackNameEvent(name="Tempo Track"))
tra.addEvent(EndOfTrackEvent(deltaTime=7680))

tra2 = Track()
tra2.addEvent(TrackNameEvent(name="New Instrument"))
tra2.addEvent(NoteOnEvent(note=0x3e, velocity=100))
tra2.addEvent(NoteOffEvent(deltaTime=190, note=0x3e, velocity=0))
tra2.addEvent(EndOfTrackEvent(deltaTime=7490))

head.addTrack(tra)
head.addTrack(tra2)

work.write(head.__str__())
work.close()