
def initialize():
    f = open("day5.txt", "r")
    nums = f.read().split(',')
    print("code recieved: " + str(nums))
    print("updating code...")
    nums = list(map(int,nums))
    print(nums[-1])
    return nums
    
  
def opcode(nums, i):
        
        
        #generate parameters
    try:
        if nums[i]//100%10 == 1:
            param_1 = nums[i+1]
        elif nums[i]//100%10 == 0:
            param_1 = nums[nums[i+1]]
    except:
        pass
    
    try:
        if nums[i]//1000%10 == 1:
            param_2 = nums[i+2]
        elif nums[i]//1000%10 == 0:
            param_2 = nums[nums[i+2]] 
    except:
        pass
    





    if nums[i]%100  == 1:
        print("adding...")
        
        
        nums[nums[i+3]] = param_1 + param_2
        #print(nums)

        opcode(nums, i+4)
    elif nums[i]%100 == 2:
    
        print("multiplying...")
        nums[nums[i+3]] = param_1 * param_2
        #print(nums)

        opcode(nums, i+4)
    
    elif nums[i]%100 ==  3:
    
        print(f"storing input at {nums[i+1]}...")
        nums[nums[i+1]]= int(input())
        
        opcode(nums, i+2)
            
    elif nums[i]%100 ==  4:

        print(f"outputting from {nums[i+1]}")
        if nums[i]//100%10 == 0:
            print(nums[nums[i+1]])
        elif nums[i]//100%10 == 1:
            print(nums[i+1])

        opcode(nums, i+2)
        
    elif nums[i]%100 == 5:
        
        print("jump if true...")
        
        if param_1 != 0:   
            opcode(nums,param_2)
        else:
            opcode(nums,i+3)

    elif nums[i]%100 == 6:
        
        print("jump if false...")

        
        if param_1 == 0:   
            opcode(nums,param_2)
        else:
            opcode(nums,i+3)
    
    elif nums[i]%100 == 7:    
        
        print("is less than?")
            
        if param_1 < param_2:
            nums[nums[i+3]]=1
        else:
            nums[nums[i+3]]=0
        
        opcode(nums,i+4)
        
    elif nums[i]%100 == 8:
    
        print("is equal?")
            
        if param_1 == param_2:
            nums[nums[i+3]]=1
        else:
            nums[nums[i+3]]=0   
    
    
        opcode(nums,i+4)
        
        
        
    elif nums[i]%100 ==  99:

        print("ending...")
        #print(nums)
        #f.close()

    else:
        print("program failure")
        print(nums)
        print(f"final position: {i}")
    
def test_sequences():
    test_1 = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]   #if input==0, =>0 else: =>1
    test_2 = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]        #     "           "
    test_3 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
                    #999 if less than 8, 1000 if equal, 1001 if greater
    tests = [test_1,test_2,test_3]
    
    
    for test in tests:
        opcode(test,0)
    print("end of tests")
    
#test_sequences()    
    
    
opcode(initialize(),0)
