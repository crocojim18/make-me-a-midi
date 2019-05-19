from functions import *
from events import *
from structures import *

work = open("out.mid", 'wb')

head = Header()

tra = Track()
tra.addEvent(TempoEvent())
tra.addEvent(EndOfTrackEvent())

head.addTrack(tra)

work.write(head.__str__())
work.close()