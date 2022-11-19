import jwt
SECRET_KEY = ""

encoded = jwt.encode({'username': 'admin', 'admin': True}, SECRET_KEY, algorithm='none')

print (encoded)

#I changed the algorithm from HS256 TO none and i got this {"response":"Welcome admin, here is your flag: crypto{The_Cryptographic_Doom_Principle}"}
#phillip helped with this lab in class also