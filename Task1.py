import csv

def read_ts(file_ptr):
    file_ptr.seek(0)
    file_ptr.readline()
    column=[]

    for line in file_ptr:
        values=line.split(",")
        column.append(values[0])
            
    return column
    

file = open("gendata.csv","r")
print(read_ts(file))
file.close()