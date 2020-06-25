# Creating a file
# Source: https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# file_object  = open('filename', 'mode') where file_object is the variable to add the file object. 
# The modes are: 

# 'r' - Read mode which is used when the file is only being read 
# 'w' - Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated) 
# 'a' - Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end 
# 'r+' - Special read and write mode, which is used to handle both actions when working with a file 

#f =open('workfile', 'w')


#Create file

file  = open('testfile.txt','w')
file.write("Hello world!\n")
file.write("This is our nextext file\n")
file.write("and this is another line\n")
file.write("Why? Because we can\n")

file.close()

#Reading file text in python

file = open('testfile.txt','r')
#print(file.read())#si se pasa un numero como argumento a read se imprimen el numero de caracteres.
#print file.readline()#cada uno de los siguientes print es una linea diferente.
#print file.readline()
#print file.readline()


for line in file:
    print line

file.close()