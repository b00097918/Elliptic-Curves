def gcd(a, b):
    
	while( b != 0 ):
		Remainder = a % b;
		a = b;
		b = Remainder;
	return a;

g = gcd(66528,52920)
print (g)