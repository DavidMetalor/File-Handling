file=open("Sample.txt", "r")
print(file.read())
file.close()

file=open("Sample.txt", "w")
print(file.write("This file has been corrupted."))
file.close()

file=open("Sample.txt", "a")
print(file.write("\n This file has also been appended"))
file.close()