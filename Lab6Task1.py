import csv

def f_stats(file_reference,file_name):
    print(file_name)
    file = open(file_name,file_reference)
    count=0
    for line in file:
        count+=1
        if(count<10):
            print(line)
    
    print(count)
    file.close()

filename="Gendata.csv"
filereference="r"
f_stats(filereference,filename)