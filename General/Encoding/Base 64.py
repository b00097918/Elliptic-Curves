#Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using 64 characters. One character of a Base64 string encodes 6 bits, and so 4 characters of Base64 encode three 8-bit bytes.

#Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.

#Take the below hex string, decode it into bytes and then encode it into Base64.


import base64

hex_values = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf" #here are the hex values that will be decoded

tmp = bytes.fromhex(hex_values) #here is the code that will decode the values 

flag = base64.b64encode(tmp).decode('utf-8')

print(flag)

