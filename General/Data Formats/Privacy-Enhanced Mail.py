from Crypto.PublicKey import RSA #imports packages

pem_file = 'C:\\Users\\John\\Desktop\\Cryptography & Secure Comms\\Cryptohack\\General\\Data Formats\\Privacy-Enhanced Mail\\lab.pem' #location of pem file 
f = open(pem_file,'r') #opens/reads RSA
key = RSA.import_key(f.read()) #imports rsa and reads

print(key.d) #prints out RSA key 