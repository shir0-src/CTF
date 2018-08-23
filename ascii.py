# !/usr/bin/env python3
import sys
import struct


def encode(arch, string):
	EncodedString = []

	for i in range(0, len(string)):
		EncodedString.append(hex(ord(string[i])).strip("0x"))

	if  arch == '-x86':
		for i in range(0, len(string), 4):
			Bytes = ""
			if  abs(i - len(string)) < 4:
				for j in range(i, len(string))[::-1]:
					Bytes += EncodedString[j]
					zerofill = "00"*(4-(len(string)-i))
				print("'{0}'==>'0x{1}{2}'".format(string[i:len(string)], zerofill, Bytes))
			else:
				for j in range(0, 4)[::-1]:
					Bytes += EncodedString[i+j]
				print("'{0}'==>'0x{1}'".format(string[i:i+4], Bytes))	
					
	elif arch == '-x64':
		for i in range(0, len(string), 8):
			Bytes = ""
			if  abs(i - len(string)) < 8:
				for j in range(i, len(string))[::-1]:
					Bytes += EncodedString[j]
					zerofill = "00"*(8-(len(string)-i))
				print("'{0}'==>'0x{1}{2}'".format(string[i:len(string)], zerofill, Bytes))
			else:
				for j in range(0, 8)[::-1]:
					Bytes += EncodedString[i+j]
				print("'{0}'==>'0x{1}'".format(string[i:i+8], Bytes))		
	
	else:
		print("Unsupported arch")
		sys.exit(0)
	

def main():
	if len(sys.argv) <  3:
		print("usage: ascii.py [option] [string]")
		print("ex1) python ascii.py -x86 ABCD")
		print("ex2) python ascii.py -x64 ABCDEFGH")
		sys.exit(0)
	arch = sys.argv[1]
	string = sys.argv[2]
	encode(arch, string)

	
if __name__ == "__main__":
	main()

