def avg(val1,val2,val3):
    if type(val1) == type("str") or type(val2) == type("str") or type(val3) == type("str"):
        return "error"
    average = (val1 + val2 + val3) / 3
    return average

arg1=1000
arg2='ABC'
arg3=50.6
print(avg(arg1,arg2,arg3))