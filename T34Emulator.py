#################################################################################################################################
#Program One: 	T34 Emulator 													#
#Name:			Kendra Deziel 												#
#Class:			CSC 317 - Computer Org & Arch 										#
#Professor:		Dr. Karlsson 												#
#Purpose:		This program is a T34 emulator with 4096 words of memory in which to store program information.		#
#				The program can be run on terminal with the command "python T34.py <your_input_file>". After 	#
#				being run, it will read the file and automatically print a memory dump. Then it will ask the 	#
#				user if they would like to use the Parsing Function. If they type y, it will prompt for a first #
#				address then prompt for a second address. If they type anything else, the program will exit. 	#
#Notes:			T34 Emulator was written and tested in Sublime environment on mac Sierra v 12.10.6  with Python v 2.7.	#
#				It has also been tested on Red Hat v 4.8.5-16 with Python 2.7 and reformatted to look nice in 	#
#				gedit text editor.										#
#################################################################################################################################

import fileinput
import sys

memory = []
address = 0
numElements = 0
ProgramCounter = 0

#################################################################################################################################
#The MemoryDump Function outputs all memory locations and corresponding information ONLY WHERE information exists. Each	memory 	#
#		location which contains "0" will be skipped. 									#
#################################################################################################################################
def MemoryDump():
	print "\n\tMemory Dump"
	for i in range(0, 4096):
		if memory[i] != 0:
			hexString =  "{:0{width}x}".format(i, width=3)
			memString =  "{:0{width}x}".format(memory[i], width=6)
			pString = hexString + ':\t'+ memString
			print pString
	print "\n"

#################################################################################################################################
#The ParsingFunction Function gives binary info for a sequence of memory locations. The binary is broken down into ADDR 	#
#		(operand address), OP (opcode), and AM (addressing mode). The input is two ints that represent the address 	#
#		location where this info can be found.										#
#################################################################################################################################
def ParsingFunction(one, two):
	#print a header 
	print "\n\tADDR\t\tOP\tAM"

	#going to use all address between one and two, including one and two
	for i in range(one, two + 1):

		#format address to a 3-digit hex and memory info to a 24-digit binary
		hexString =  "{:0{width}x}".format(i, width=3)
		binString = "{0:024b}".format(memory[i])

		#break the binary string so ADDR is 12 bits, OP is 6 bits, and AM is 6 bits
		print hexString + ':\t' + binString[:12] + '\t' + binString[12:-6] + '\t' + binString[18:]
	print "\n"

#################################################################################################################################
#The Main Function reads the input file, puts each program info into the appropriate memory location, sets the Program Counter,	#
#		and controls the user's access to the ParsingFunction. It is complete with input error checking and the entire	#
#		program will terminate when user input dictates an end to use of the Parsing Function.				#
#################################################################################################################################
def Main():
	with open(sys.argv[1], "r") as inp:
		for line in inp:

			nums = line.split(' ')

			if len(nums) < 3:
				ProgramCounter = nums[0]
				MemoryDump()
				useParser = raw_input("Utilize Parsing Function? (y/other): ").upper()

				while(useParser == "Y" or useParser == "YES" ):

					#make sure user inputs an int both times, otherwise start over
					try:
						addressOne = int(raw_input("First Address in Base 10: "))
					except:
						useParser = raw_input("Wanna try that again? (y/other): ").upper()
						continue

					try:
						addressTwo = int(raw_input("Second Address in Base 10: "))
					except:
						useParser = raw_input("Wanna try that again? (y/other): ").upper()
						continue

					ParsingFunction(addressOne, addressTwo)
					useParser = raw_input("Utilize Parsing Function? (y/other): ").upper()

				return

			else:
				address = int(nums[0], 16)

				numElements = int(nums[1])

				for el in range(0, numElements):
					memory[address + el] = int(nums[2 + el], 16)


#fill array with 4096 "0"s to represent empty memory
for j in range(0, 4096):
	memory.append(0)

#Main will call MemoryDump and ParsingFunction functions
Main()

