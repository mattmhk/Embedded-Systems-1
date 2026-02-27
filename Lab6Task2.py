import csv

file = open("Gendata.csv","r")
file.readline()
count=0
linenumber=1

for line in file:
    values=line.split(",")
    linenumber+=1
    try:
        float(values[1])
    except:
        continue
    else:
        if count==0:
            max=float(values[1])
            min=float(values[1])
            count+=1
        else:
            if float(values[1])>max:
                max=float(values[1])
                maxline=linenumber
            if float(values[1])<min:
                min=float(values[1])
                minline=linenumber
file.close()
print("Max value is "+str(round(max,2))+"MW in line "+str(maxline))
print("Min value is "+str(round(min,2))+"MW in line "+str(minline))