import array
import math
import random

#A function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#Main program starts here
#Ask and verify input for length of password
passwordValid = False
while (passwordValid == False):
    passwordLength = int(input ("Please enter a number between 8 and 32 for password length:\n"))
    passwordValid = bool(8 <= int(passwordLength) <= 32)

print("Requested password length is: ", passwordLength)

#Create limits of amount of each type of character in the password
numUppercaseLetters = int(passwordLength / 3)
numLowercaseLetters = int(numUppercaseLetters)
numDigits = int((passwordLength - numUppercaseLetters - numLowercaseLetters) * .6)
numPunctuation = int(passwordLength - numUppercaseLetters - numLowercaseLetters - numDigits)

print("Number of Uppercase Letters:", numUppercaseLetters)
print("Number of Lowercase Letters:", numLowercaseLetters)
print("Number of Digits:", numDigits)
print("Number of Punctuation:", numPunctuation)

#Create a list of all of the characters to be used
uppercaseLetters = ['']
lowercaseLetters = ['']
digits = ['']
punctuations = ['']

for _ in range(numUppercaseLetters):
    uppercaseLetters.append(chr(random.randint(65,90))) #Generate a random Uppercase Letter (based on ASCII code)

for _ in range(numLowercaseLetters):
    lowercaseLetters.append(chr(random.randint(97,122))) #Generate a random Lowercase Letter (based on ASCII code)

for _ in range(numDigits):
    digits.append(chr(random.randint(48,57))) #Generate a random digit from 0 to 9 (based on ASCII code)

for _ in range(numPunctuation):
    punctuations.append(chr(random.randint(33,47))) #Generate a random punctuation character (based on ASCII code)

#Generate password using all the characters, in random order
passwordCharacters = uppercaseLetters + lowercaseLetters + digits + punctuations

password = ""
for _ in passwordCharacters:
    password += _

password = shuffle(password)

#Output
print(password)
