import re

#input: array of positive integers < 255 representing an integer using variable length quantity
#output: integer representation of that array, < 0FFFFFFF
def vl2int(arr):
	smallArr = []
	kill = False
	index = 0
	toReturn = ''
	while not kill:
		if arr[index] < 128: kill = True
		stri = bin(arr[index])[2:]
		while len(stri) < 8:
			stri = '0'+stri
		smallArr.append(stri[1:])
		index+=1
	for i in smallArr:
		toReturn += i
	return int(toReturn, 2)
	
def int2vl(num):
	strRep = bin(num)[2:]
	overlap = len(strRep) % 7
	arr = []
	if overlap > 0:
		arr.append(strRep[0:overlap])
		strRep = strRep[overlap:]
	while strRep != "":
		arr.append(strRep[0:7])
		strRep = strRep[7:]
	index = 0
	while index < len(arr):
		if index < len(arr)-1:
			toAdd = '1'
			while len(toAdd)+len(arr[index])<8:
				toAdd += "0"
			arr[index] = int(toAdd + arr[index], 2)
		else:
			toAdd = '0'
			while len(toAdd)+len(arr[index])<8:
				toAdd += "0"
			arr[index] = int(toAdd + arr[index], 2)
		index += 1
	return bytearray(arr)

def byte2str(byt):
	toReturn = "[ "
	for i in byt:
		toReturn += str(int(i))
		toReturn += " "
	toReturn += "]"
	return toReturn
	
def int2bin(num, byteNum):
	newNum = bin(num)[2:]
	if num >= 2**(byteNum*8):
		print "Passed value too large for {} byte space.".format(byteNum)
		return
	overlap = len(newNum) % 8
	arr = []
	if overlap > 0:
		arr.append(int(newNum[0:overlap],2))
		newNum = newNum[overlap:]
	while newNum != "":
		arr.append(int(newNum[0:8],2))
		newNum = newNum[8:]
	arr = bytearray(arr)
	while len(arr) < byteNum:
		arr = bytearray([0]) + arr
	return arr

def note2int(note):
	key = note[0]
	extra = ''
	note = note[1:]
	if note[0] in ['#', 'b']:
		extra += note[0]
		note = note[1:]
	octave = note
	if re.match(r'^[a-gA-G][#b]?$',key+extra) == None:
		print "Invalid note "+key+extra+octave+"."
		return
	if re.match(r'^(-1|[0-9])$',octave) == None:
		print "Invalid note "+key+extra+octave+"."
		return
	toReturn = 0
	if key in ['d','D']: toReturn = 2
	elif key in ['e','E']: toReturn = 4
	elif key in ['f','F']: toReturn = 5
	elif key in ['g','G']: toReturn = 7
	elif key in ['a','A']: toReturn = 9
	elif key in ['b','B']: toReturn = 11
	
	if extra == 'b': toReturn -= 1
	elif extra == '#': toReturn += 1

	toReturn = ((int(octave)+1)*12)+toReturn
	
	if 0 <= toReturn < 128:
		return toReturn
	else:
		print "note "+key+extra+octave+" not supported."
		return
