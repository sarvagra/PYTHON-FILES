# writing a binary file
# in case of  binary file use "rb" and "wb" to read and write respectively-


with open("text.bin", "wb") as f :
    f.write(b"\x01\x02\x03")

# reading a binary file


with open("text.bin", "rb") as f :
    print(f.read())

