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
key=Fernet.generate_key()#Fernet.generate_key generates a hash which is used for encrypting.
with open("Thekey.key","wb") as mykey:#writing the generated key to a file name Thekey.key
    mykey.write(key)
    mykey.close

for file in files: #Opening a for loop used to encrypt the files is the files array.
    with open(file,"rb") as myfiles: #using open() reading files in the array files.
        content=myfiles.read() #reading the content in the text file and storing in variable content.
        encrypted_content=Fernet(key).encrypt(content)#using fernet encrypting the content using the key.

    with open(file,"wb") as myfiles:#using open() overwriting the files in the directory.
        myfiles.write(encrypted_content)