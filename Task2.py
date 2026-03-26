import csv
import matplotlib.pyplot as plt

def read_col(file_ptr,column_num):
    file_ptr.seek(0)
    file_ptr.readline()
    column=[]

    for line in file_ptr:
        values=line.split(",")
        try:
            float(values[column_num-1])
        except:
            column.append(-100)
        else:
            column.append(float(values[column_num-1]))
            
    return column

file = open("testdata.csv","r")
    
plt.plot(read_col(file, 2), color='blue')
plt.xlabel('Time (samples)')
plt.ylabel('Turbine 1 (MW)')
plt.title('Generated Output from Turbine 1')
plt.legend()
plt.show()

plt.plot(read_col(file, 3), color='green')
plt.xlabel('Time (samples)')
plt.ylabel('Turbine 2 (MW)')
plt.title('Generated Output from Turbine 2')
plt.legend()
plt.show()

plt.plot(read_col(file, 4), color='red')
plt.xlabel('Time (samples)')
plt.ylabel('Turbine 3 (MW)')
plt.title('Generated Output from Turbine 3')
plt.legend()
plt.show()

plt.plot(read_col(file, 5), color='black')
plt.xlabel('Time (samples)')
plt.ylabel('Turbine 4 (MW)')
plt.title('Generated Output from Turbine 4')
plt.legend()
plt.show()

file.close()


