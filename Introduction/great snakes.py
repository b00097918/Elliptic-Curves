






#!/usr/bin/env python3
ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))

#You have to take away the import of the system part of the code, once you do that run the file that is given in the description and it will give you the flag