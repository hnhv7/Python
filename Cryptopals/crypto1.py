import logging
import sys
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logging.debug('Start of program')


#############################################
#
#  Takes in a hex number and returns
#        a binary number
#
#############################################
                    
def hex2bin(number):
  binnum = ""
  binholder = ""
  
  for i in number:                     # Loop takes first number in hex number
    if i == "a" or i == "A":           # and checks whether it's A-F
      binnum = binnum + "1010"         # If it isn't, uses bin() function
    elif i == "b" or i == "B":         # and trims off "0b" then adds padding 0s
      binnum = binnum + "1011"         # if necessary
    elif i == "c" or i == "C":
      binnum = binnum + "1100"
    elif i == "d" or i == "D":
      binnum = binnum + "1101"
    elif i == "e" or i == "E":
      binnum = binnum + "1110"
    elif i == "f" or i == "F":
      binnum = binnum + "1111"
    else:
      binholder = bin(int(i))[2:]
      binholder = binholder.rjust(4,"0")
      binnum = binnum + binholder
  return binnum

#############################################
#
#  Takes in a binary number and returns
#        a Base-64 number
#
#############################################

def bin2base64(binnum):
  base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-"
  count = 0
  final = ""

  while count < len(binnum):              # Grabs 6 bits at a time
    temp = binnum[count:count + 6:1]      # and converts them into Base-64
    temp = int(temp, 2)                   # Then adds it to return value, "final"
    holder = base64[temp]
    final = final + holder
    count = count + 6
  return final


#############################################
#
#  Takes in a hex number and returns
#        a Base-64 number
#
#############################################

def hex2base64(number):
  binnum = hex2bin(number)
  return_value = bin2base64(binnum)
  return return_value
  



try:
  loopnum = int(input("How many numbers would you like to enter? "))
except ValueError:
  print("Please enter a valid selection.")
  
  
while (loopnum != 0):
  loopnum = loopnum - 1
  number = input("Enter a hex number: ")
  for num in number:
    if num not in "0123456789abcdefABCDEF":
      print("you chose an invalid number")
      sys.exit()
  print ("That number in Binary is: " + hex2bin(number))
  print ("That number in Base-64 is: " + hex2base64(number))


