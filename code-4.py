range_low  = "264793"
range_high = "803935"



positions = [0,1,2,3,4]

def check_doubles(code):
    for pos in positions:
        if code.count(code[pos])==2:
            return(True)
    return(False)        
    

def check_increasing(code):
    for pos in positions:
        if code[pos] > code[pos+1]:
            return(False)
    return(True)


#main process
search_lis = []
numbers_to_check = int(range_high)-int(range_low)
print(f"Remaining combinations: {numbers_to_check}")

#make the original list
for code in range(int(range_low),int(range_high)):
    code = str(code)
    if check_doubles(code) and check_increasing(code): 
        search_lis.append(code)
        
    numbers_to_check -= 1
    if numbers_to_check%100 == 0:
        print(f"Remaining combinations: {numbers_to_check}")

        


print(f"Total number of codes = {len(search_lis)}")
