# buffer read and write (writes bigger files in 'chunks')
# writing
import io 
with open("test1.txt","wb") as f :
    file = io.BufferedWriter(f)

    file.write(b"this is my first line\n")
    file.write(b"this is my second line\n")
    file.flush()

 #reading 
with open("test1.txt","rb") as f :
    file = io.BufferedReader(f)
    data=file.read()
    print(data)
    
#we can choose the amount of data to be read by writing amount of bytes in file.read() brackets

    data1=file.read(1000)
    print(data1)
    #reads data upto 1000 bytes and displays it 