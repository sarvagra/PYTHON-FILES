# im going to implement logging in a code which filters strings and integers from a given list

#creating logger to log the data

import logging
logging.basicConfig(filename="SORT_LOGS.log", level= logging.DEBUG, format='%(asctime)s %(message)s')

# implementing into code to store logs step by step

l=[1,2,3,"this",0,"is",99,"me","learning",34,44,23,56,"coding"]
l_int=[]
l_str=[]

for i in l :
    logging.info("entered into loop and checking condition")
    
    if type(i) is int:
        l_int.append(i)
        logging.info("added int file into l_int list")

    if type(i) is str:        
        l_str.append(i)
        logging.info("added string file into l_str list")
    
logging.info("this is the integer list :{l1} and this is the string list {l2}".format(l1=l_int, l2=l_str))