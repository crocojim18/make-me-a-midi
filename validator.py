#validator.py

import json

from midiFunctions import *
from events import *
from structures import *
from musicFunctions import *

def test(testString, actual, expected, filename, errorDict):
	succeed = False
	if filename not in errorDict:
		errorDict[filename] = {"SUCCEEDED":{}, "FAILED":{}}
	if type(actual) != type(expected):
		succeed = False
	elif isinstance(actual, int) or isinstance(actual, str):
		if actual == expected: succeed = True
	elif isinstance(actual, bytearray):
		if len(actual) != len(expected):
			succeed = False
		else:
			succeed = True
			for i in range(len(actual)):
				if actual[i] == expected[i]:
					succeed = succeed and True
				else:
					succeed = False
	elif actual == None and expected == None:
		succeed = True
	
	if isinstance(actual, bytearray):
		actual = byte2str(actual)
	if isinstance(expected, bytearray):
		expected = byte2str(expected)
	
	if not succeed:
		errorDict[filename]['FAILED'][testString] = {"EXPECTED":expected, "ACTUAL":actual}
	else:
		errorDict[filename]['SUCCEEDED'][testString] = {"EXPECTED":expected, "ACTUAL":actual}
	
errors = {}

testing = "midiFunctions.vl2int"

print "Testing "+testing
test('vl2int(bytearray([0x03,0x68]))',vl2int(bytearray([0x03,0x68])), 3, testing, errors)
test('vl2int(bytearray([0x9F,0xA2,0x00]))',vl2int(bytearray([0x9F,0xA2,0x00])), 0x07D100, testing, errors)
test('vl2int(bytearray([0x87,0x68]))',vl2int(bytearray([0x87,0x68])), 1000, testing, errors)
test('vl2int(bytearray([0xFF,0xFF,0xFF,0x7F]))',vl2int(bytearray([0xFF,0xFF,0xFF,0x7F])), 268435455, testing, errors)
test('vl2int(bytearray([0xFF,0xFF,0xFF,0x80]))',vl2int(bytearray([0xFF,0xFF,0xFF,0x80])), None, testing, errors)
test('vl2int(bytearray([0xFF,0xFF,0xFF,0x80,0x03]))',vl2int(bytearray([0xFF,0xFF,0xFF,0x80,0x03])), None, testing, errors)

testing = "midiFunctions.int2vl"
print "Testing "+testing
test('int2vl(4)',int2vl(4), bytearray([0x4]), testing, errors)

print(json.dumps(errors, indent=4, sort_keys=True))