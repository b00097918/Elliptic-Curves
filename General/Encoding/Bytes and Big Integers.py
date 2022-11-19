#Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?

#The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16 number, and also represented in base-10.



from Crypto.Util.number import long_to_bytes #in the description it tells you to use crytpo and long to bytes
Hex = 11515195063862318899931685488813747395775516287289682636499965282714637259206269 #this is the hex string that will be decoded 
flag = long_to_bytes(Hex).decode('utf-8') #This will decode the hex number
print(flag) #this will print out the Flag

