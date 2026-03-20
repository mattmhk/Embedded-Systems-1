import csv
import matplotlib.pyplot as plt

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
            column.append(float(values[columnNo-1]))
            
    file.close()
    return column

l1=columnToList("gendata.csv",2)
l2=columnToList("gendata.csv",3)
l3=columnToList("gendata.csv",4)
l4=columnToList("gendata.csv",5)

result=[a+b+c+d for a,b,c,d in zip(l1,l2,l3,l4)]

plt.plot(result, color='Green')
plt.xlabel('Time')
plt.ylabel('Output (MW)')
plt.title('Power Station Output from Turbines 1, 2, 3, and 4')
plt.legend()
plt.show()
