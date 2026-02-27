import csv

file = open("Gendata.csv","r")
file.readline()
sum=0
linenumber=1

for line in file:
    values=line.split(",")
    linenumber+=1
    try:
        float(values[1])
    except:
        continue
    else:
        sum+=float(values[1])
file.close()
print("Average value is "+str(round(sum/(linenumber),2))+" MW")