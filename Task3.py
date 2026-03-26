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

turbine1 = read_col(file, 2)
turbine2 = read_col(file, 3)
turbine3 = read_col(file, 4)
turbine4 = read_col(file, 5)

average_output = [(a+b+c+d)/4 for a,b,c,d in zip(turbine1,turbine2,turbine3,turbine4)]

plt.plot(average_output, color='blue')
plt.xlabel('Time (samples)')
plt.ylabel('Average Output (MW)')
plt.title('Average Power Station Output')
plt.legend()
plt.show()

file.close()