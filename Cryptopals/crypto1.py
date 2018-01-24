import logging
import sys
#ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-
logging.basicConfig(level=logging.CRITICAL, format='%(message)s')
logging.debug('Start of program')

                    
def hex2bin(number):
  base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-"
  binnum = ""
  count = 0
  newWord = ""
  final = ""
  binholder = ""
  
  for i in number:
    if i == "a" or i == "A":
      binnum = binnum + "1010"
    elif i == "b" or i == "B":
      binnum = binnum + "1011"
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
    logging.debug('binholder:' + str(binholder))
    
  while count < len(binnum):
   newWord = binnum[count:count+6:1]
   logging.debug('binnum:' + str(binnum))
   newWord = int(newWord, 2)
   logging.debug('newWord:' + str(newWord))
   holder = base64[newWord]
   logging.debug('holder :' + str(holder))
   final = final + holder
   count = count +6

  return final
      


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
  print ("That number in Base-64 is: " + hex2bin(number))


