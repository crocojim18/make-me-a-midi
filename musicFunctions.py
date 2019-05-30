class Link:
	def __init__(self,name,syn=None):
		self.name = name
		self.synonyms = syn
		self.next = None
		self.prev = None
		
	def setNext(self, link):
		self.next = link
		link.prev = self
		
	def setPrev(self, link):
		self.prev = link
		link.next = self

class COF:
	def __init__(self):
		self.majPattern = '2212221'
		self.minPattern = '2122122'
		
		self.a = Link('a')
		self.ash = Link('a#',syn="bb")
		self.b = Link('b',syn="cb")
		self.c = Link('c',syn="b#")
		self.csh = Link('c#',syn="db")
		self.d = Link('d')
		self.dsh = Link('d#',syn="eb")
		self.e = Link('e',syn="fb")
		self.f = Link('f',syn="e#")
		self.fsh = Link('f#',syn="gb")
		self.g = Link('g')
		self.gsh = Link('g#',syn="ab")

		self.a.setNext(self.ash)
		self.ash.setNext(self.b)
		self.b.setNext(self.c)
		self.c.setNext(self.csh)
		self.csh.setNext(self.d)
		self.d.setNext(self.dsh)
		self.dsh.setNext(self.e)
		self.e.setNext(self.f)
		self.f.setNext(self.fsh)
		self.fsh.setNext(self.g)
		self.g.setNext(self.gsh)
		self.gsh.setNext(self.a)
		
		self.notes = {
			"a": self.a, 
			"a#": self.ash,
			"bb": self.ash,
			"b": self.b,
			"b#": self.c,
			"cb": self.b,
			"c": self.c, 
			"c#": self.csh, 
			"db": self.csh,
			"d": self.d,
			"d#": self.dsh, 
			"eb": self.dsh,
			"e": self.e, 
			"e#": self.f,
			"fb": self.e,
			"f": self.f, 
			"f#": self.fsh, 
			"gb": self.fsh,
			"g": self.g,
			"g#": self.gsh,
			"ab": self.gsh
			}

	def getScale(self,key,scale):
		toReturn = []
		curr = self.notes[key.lower()]
		pattern = self.majPattern
		if scale.lower() in ["min","minor"]:
			pattern = self.minPattern
		toPick = key.lower()[0]
		for i in pattern:
			#print toPick
			if curr.name[0] == toPick:
				toReturn.append(curr.name)
				#print curr.name
			elif curr.synonyms != None and curr.synonyms[0] == toPick:
				toReturn.append(curr.synonyms)
				#print curr.synonyms
			else:
				print "Key currently not supported"
				return
			if i == '1':
				curr = curr.next
			elif i == '2':
				curr = curr.next.next
			if toPick == 'g': toPick = 'a'
			else: toPick = chr(ord(toPick) + 1)
		return toReturn