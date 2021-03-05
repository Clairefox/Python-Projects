#What is a Ceasar cipher? https://en.wikipedia.org/wiki/Caesar_cipher

#Initialize Variables
plainText = (input("Please enter a sentence to encrypt:\n")).upper()

shiftValid = False
while (shiftValid == False):
    shift = int(input("Please enter a number by which to 'shift' each letter from 1 to 26:\n"))
    shiftValid = bool(1<= int(shift) <= 26)

print("Original string:\n", plainText)

#Convert each chr to its ASCII value
plainASCII = []
for _ in plainText:
    plainASCII.append(ord(_))

print("Original string in ASCII code:\n", plainASCII)

#Shift each ASCII value
shiftedASCII = []
for _ in plainASCII:
    if (65 <= _ <= (90 - shift)):
        shiftedASCII.append(_ + shift)
    elif ((90 - shift) < _ <= 90):
        shiftedASCII.append(64 + (shift - (90 - _)))
    else:
        shiftedASCII.append(_)

print("Encrypted string in ASCII code:\n", shiftedASCII)

#Convert each ASCII value back to chr
encryptedASCII = ""
for _ in shiftedASCII:
    encryptedASCII += chr(_)

print("Encrypted string:\n", encryptedASCII)