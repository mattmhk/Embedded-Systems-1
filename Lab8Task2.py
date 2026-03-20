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
    
plt.plot(columnToList("gendata.csv", 2), color='black')
plt.xlabel('Time')
plt.ylabel('Turbine 1 (MW)')
plt.title('MW Output from Turbine 1')
plt.legend()
plt.show()


