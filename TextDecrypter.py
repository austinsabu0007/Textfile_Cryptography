import os #os module is used to access the files and modify files in system.
from cryptography.fernet import Fernet #Fernet is used to generate unique key and encrypt and decrypt files with it.

files=[] #declaring an array
for file in os.listdir(): #os.listdir() is used to list the files in the folder.
    if file=="TextEncrypter.py" or file=="TextDecrypter.py" or file=="Thekey.key":
        continue
    if os.path.isfile(file):#os.path.isfile() is used to check the provided file is an actual existing file.
        files.append(file)#append() is used for append or store the data in file to files(array).
"""The above for loop is used to store the files in the directory to the files array.
   This follows some conditions.
   * If the file named is TextEncrypter,Thekey,Textdecrypter then never saves of files.
   * If there is a folder in directory the also never stores that."""
with open("Thekey.key", "rb") as mykey:#Reading the key from file Thekey.key and stores in key.
    key=mykey.read()

for file in files:
    with open(file,"rb") as myfiles:
        content=myfiles.read()
        decrypted_content=Fernet(key).decrypt(content)#decrypting the contents in files.

    with open(file,"wb") as myfiles:# overwriting the decrypted contents to the files.
        myfiles.write(decrypted_content)

