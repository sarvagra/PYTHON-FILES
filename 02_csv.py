# reading and writing a comma separated data 
import csv

data1=[["NAME","EMAIL","PHONE"],
       ["Sarvagra","sarvagras977@gmail.com","7348650236"],
       ["Ex","ex123@gmail.com","2237154590"]
      ]
with open("data1.csv", "w") as f :
    writer = csv.writer(f)

    for i in data1:
        writer.writerow(i)

with open("data1.csv", "r") as f :
    read_data =csv.reader(f)
    for i in read_data :
        print(i)

with open("text.bin", "wb") as f :
    f.write(b"\x01\x02\x03")