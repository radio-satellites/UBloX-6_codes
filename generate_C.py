filename = input("Command name to write: ")
arrayName = input("Array name (in C): ")

f = open(filename+".txt",'r')

start = "const PROGMEM  uint8_t "+str(arrayName)+"[] = {"
end = "};"

bytes_data = []

length = len(f.read())

f.close()
f = open(filename+".txt",'r')
#Yikes... sorry...

for i in range(int(length/2)):
    byte = f.read(2)
    CByte = "0x"+str(byte)
    bytes_data.append(CByte)
##Build array
middle = str(bytes_data).replace("[","").replace("]","").replace("'","")    

array_C = start+middle+end #Voila

print("")
print("Array:")
print("")
print(array_C)
