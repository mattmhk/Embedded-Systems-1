sample_txt = """It is a long-established fact that a reader will be 
distracted by the readable content of a page when looking at its layout. The 
point of using Lorem Ipsum is that it has a more-or-less normal distribution 
of letters."""
space_no=0
dash_no=0
comma_no=0
stop_no=0
total_no=0
for i in sample_txt:
    total_no += 1
    if i == " ":
        space_no += 1
    elif i == "-":
        dash_no += 1
    elif i == ",":
        comma_no += 1
    elif i == ".":
        stop_no += 1
        
print("Number of spaces in the text:", space_no)
print("Number of dashes in the text:", dash_no)
print("Number of commas in the text:", comma_no)
print("Number of full stops in the text:", stop_no)
print("Total number of characters in the text:", total_no)