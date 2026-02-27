def num_cnt(text):
    count=0
    if type(text) != type("str"):
        return "error"
    words=text.split()
    for word in range(len(words)):
       for char in words[word]:
           if char.isdigit():
               count+=1
    return count
    

sample_txt = """1. It is a long-established fact that a reader will be 
distracted by the readable content of a page when looking at its layout. 2. 
The point of using Lorem Ipsum [1] is that it has a more-or-less normal 
distribution of letters [2] .""" 

print(num_cnt(sample_txt))