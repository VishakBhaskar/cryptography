import base58

mystring = 'hello world'
mybase58 = base58.b58encode(mystring)

print('Base58 String:')
print(mybase58)

encrypted = '5QWTsqdM9CC9on'
decrypted = base58.b58decode(encrypted)

print('Decrypted Code : ')
print(decrypted)

mynumber = 8954
myhexnumber = hex(mynumber)

print('Hex number:')
print(myhexnumber)
