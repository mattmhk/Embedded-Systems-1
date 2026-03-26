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

min_output_index = average_output.index(min(average_output))
min_output_value = min(average_output)
max_output_index = average_output.index(max(average_output))
max_output_value = max(average_output)

file.seek(0)
file.readline()
count=1
for line in file:
    values=line.split(",")
    count += 1
    if count == min_output_index:
        min_time = values[0]
    if count == max_output_index:
        max_time = values[0]

file.close()
out = open("Output.csv","w")

out.write(str(min_time) + "," + str(round(min_output_value, 8)) + "\n")
out.write(str(max_time) + "," + str(round(max_output_value, 8)) + "\n")
out.write("Myat Htet Ko, 40502621")