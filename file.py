#prgrm for file

f=open("Firstfile.txt","w")
name="Nandini"
f.write(name)
surname="Dighe"
f.write(" "+surname)
f.close()

f=open("Firstfile.txt","r")
name=f.read()
print(name)
f.close()
