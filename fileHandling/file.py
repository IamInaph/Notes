# "x" - Create - will create a file, returns an error if the file exist
f = open("data3.txt", "x")
programming = input("Write a short paragraph about programming. ")
f = open('data0.txt','w')
#f.write(programming)
f.close()

# "a" - Append - will create a file if the specified file does not exist
programming = input(" Write an another paragraph :")
f = open("data5.txt","a")
f.write(programming)
f.close()

# "w" - Write - will create a file if the specified file does not exist

programming = input("Write a paragraph about programming. ")
f = open("data5.txt", "w")
f.write(programming)
f.close()


#  Read the content of the file

f = open("data5.txt","r")

#reading entire file
print(f.read())

#reading one line
print(f.readline())

#reading all lines in the form of list 
print(f.readlines())
f.close()


#Deletion 
import os 
# how to remove a file:
os.remove("data3.txt")

# Check if file exists, then delete it:
if os.path.exists:
    os.remove("data1.txt")
else:
    print("The file does not exists.")


#how to delete a folder :

os.rmdir("test")

import os
os.remove("data1.b")

a = input("Enter your age:").encode()
f = open("data1.b",'wb')
f.write(a)


f = open("data1.txt","rb")
a = f.read()
print(a.decode())

# Get user input and convert to bytes
a = input("Enter your age:").encode()

# Write the bytes to a binary file
f=open("data1.b", 'wb') 
f.write(a)

# Read the bytes from the binary file and print as string
f = open("data1.b", "rb")
data = f.read()
print(data.decode())

# Reading and writing binary data
# 'rb+': Read and write binary – Opens a file for both reading and writing in binary mode.
f = open("data2.b","rb+")
#data = f.read()
    
#print(f"Existing data: {data.decode()}")
    
a = input("Enter your name").encode()
f.seek(12)
f.write(a)


# 'wb+': Write and read binary – Opens a file for writing and reading in binary mode. The file is created if it does not exist, and the content is erased if it does.
f = open("data2.b","wb+")
data = f.read()
    
# print(f"Existing data: {data.decode()}")
    
a = input("Enter your name").encode()
# for position 
f.seek(10)

f.write(a)
   


#'ab+': Append and read binary – Opens a file for both appending and reading in binary mode. The file is created if it does not exist.
f = open("data2.b","ab+")
data = f.read()
    
# print(f"Existing data: {data.decode()}")
    
a = input("Enter your name").encode()
f.write(a)
