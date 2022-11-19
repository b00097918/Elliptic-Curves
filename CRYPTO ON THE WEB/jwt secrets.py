import jwt
SECRET_KEY = "secret"

encoded = jwt.encode({'username': 'admin', 'admin': True}, SECRET_KEY, algorithm='HS256')

print (encoded)


#place the code that prints out in the terminal onto this website and you will ge tyou flag http://web.cryptohack.org/jwt-secrets/ 