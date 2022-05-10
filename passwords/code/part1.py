import hashlib
import binascii
import json

words = [line.strip().lower() for line in open('words.txt')]

passwords1 = [line.strip().lower() for line in open('passwords1.txt')]

print(len(words))
print(len(passwords1))

final_names = []
final_passwords = []
for password in passwords1:
  password = password.split(":")
  final_names.append(password[0])
  final_passwords.append(password[1])

cracked_name = []
cracked_pass = []

def hash(input):
    encode = input.encode('utf-8') # type=bytes
    hasher = hashlib.sha256(encode)
    digest = hasher.digest()
    digest_as_hex = binascii.hexlify(digest)
    hash = digest_as_hex.decode('utf-8') 
    return hash


print("Jeffs")
print(hash("moose"))
print ("182072537ada59e4d6b18034a80302ebae935f66adbdf0f271d3d36309c2d481" == (hash("moose")))

hashes = dict()
for w in words:
    h = hash(w)
    hashes[h] = w
    print(w)

print(len(hashes))

cracked_keys = {}
i=0
for hash in (final_passwords):
    password = hashes[hash]
    cracked_keys[final_names[i]] = password
    i = i + 1
    
print(cracked_keys)
with open('passwords1done.txt', 'w') as file:
    for name in cracked_keys.keys():
        file.writelines(name + ":" + cracked_keys[name] + "\n")
