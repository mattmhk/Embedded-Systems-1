import csv

def columnToList(filename,columnNo):
    file = open(filename,"r")
    file.readline()
    column=[]

    for line in file:
        values=line.split(",")
        try:
            float(values[columnNo-1])
        except:
            column.append(-100)
        else:
            column.append(values[columnNo-1])
            
    file.close()
    return column
    

print(columnToList("gendata.csv",2))