data = {
    "name"  : "sarvagra",
    "email" : "sarvagras977@gmail.com",
    "ph_no" : "7348650236",
    "subject" : ["data science", "big data" , "data analytics"]
        } #javascript type data

import json 
with open("data.json","w") as f:
    json.dump(data,f)
with open("data.json","r") as f:
    data= json.load(f)
data     
