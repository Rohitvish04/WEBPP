# File Handling: .txt, .pdf, .docx

#file path
filePath = "C:/Users/Picsurely/Documents/pythonfile/createFilewithWrite.txt.txt"

# open(fileLocation, mode of operation) : open aa file
# mode - read - r, write -w, update -a
file = open(filePath, 'r')  #read()
print(file.read())
file.close()

# Test - crud
# doc - crud

# create a new file - mode - w, method- write()
path = "C:/Users/Picsurely/Documents/pythonfile/createFilewithWrite.txt.txt"
# with open(path,'w') as file:
#     file.write("Hello this is our first writing operatio in file handling, thank you for watching!!")

# print("Done")

#update a file - a
# with open(path,'a') as file:
#     file.write("\nAnudip foundation")

print("done")

# reomve a file:
import os
