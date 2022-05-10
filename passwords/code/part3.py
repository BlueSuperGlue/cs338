import hashlib
import binascii
import json
 
words = [line.strip().lower() for line in open('words.txt')]
 
passwords3 = [line.strip().lower() for line in open('passwords3.txt')]
 
# print(len(words))
# print(len(passwords3))
 
def salt_hash(salt,input):
   new_input = salt+input
   encode = new_input.encode('utf-8') # type=bytes
   hasher = hashlib.sha256(encode)
   digest = hasher.digest()
   digest_as_hex = binascii.hexlify(digest)
   hash = digest_as_hex.decode('utf-8')
   return hash
 
print("Jeffs")
print(salt_hash("e75fa822","moose"))
print(salt_hash("73f5c390","moose"))
 
print ("6b5b88886d9fcd76e5c4dceafb0069cb969d4f63d331793ae78b1f9b99bdee41" == (salt_hash("73f5c390","moose")))
 
final_names = []
salts = []
final_passwords = []
hashToName = {}
for password in passwords3:
   password = password.split(":")
   final_names.append(password[0])
   salt = password[1][3:11]
   salts.append(salt)
   final_passwords.append(password[1][12:])
   hashToName[password[1][12:]] = password[0]
 
 
   # for w1 in wordlist:
   #     for w2 in wordlist:
   #         h = hash(w1 + w2)
   #         for user in password file:
   #             if h == hash for user:
   #                 yay
print("Is it in")
print(salt_hash("73f5c390","moose") in final_passwords)
#print(final_passwords)
 
namesDone = []
passwordsDone= []
 
with open('passwords3done.txt', 'w+') as passfile:
   for word in words:
       for i in range(len(salts)):
           h = salt_hash(salts[i],word)
           if h in hashToName:
               index = final_passwords.index(h)
               print(final_names[index] + ":" + word)
               # namesDone.append(final_names[i])
               # passwordsDone.append(word)
               # passfile.writelines(final_names[i] + ":" + word + "\n")
 
# with open('passwords3donebackup.txt', 'w+') as pfile:
#     for i in range(len(namesDone)):
#         passfile.writelines(namesDone[i] + ":" + passwordsDone[i] + "\n")
