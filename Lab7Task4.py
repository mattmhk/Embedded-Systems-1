import matplotlib.pyplot as plt
import csv

file = open("Gendata.csv","r")
file.readline()
linenumber=1
value=[]

for line in file:
    values=line.split(",")
    linenumber+=1
    if len(values[1])==0:
        continue
    try:
        float(values[1])
    except:
        continue
    else:
        value.append(float(values[1]))
        
file.close()
print("Lines read: "+str(linenumber))
print("Valid values read: "+str(len(value)))
plt.plot(value)
plt.show()