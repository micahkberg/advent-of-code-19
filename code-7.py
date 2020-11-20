def initialize():
    f = open("day7test1.txt", "r")
    nums = f.read().split(',')
    
    print("initializing... code recieved: ") #+ str(nums))
    print("updating code...")
    
    nums = list(map(int,nums))

    return nums
    
  
def opcode(nums, i, input_on_load):
    print(f"input sequence: {input_on_load}")
        
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
        instruction_length = 4
        
    elif nums[i]%100 == 2:
    
        print("multiplying...")
        nums[nums[i+3]] = param_1 * param_2
        #print(nums)
            
        instruction_length = 4
    
    elif nums[i]%100 ==  3:
    
        print(f"storing input at {nums[i+1]}...")
        
        if input_on_load != None or input_on_load != []:
            nums[nums[i+1]]= input_on_load[0]
            input_on_load = input_on_load[1:]
        else:
            nums[nums[i+1]]= int(input())
        
        
        instruction_length = 2
       
            
    elif nums[i]%100 ==  4:
        
        print(f"outputting from {nums[i+1]}")
        
        
        ###         commented out code is for when the output isn't linked to anything
        #if nums[i]//100%10 == 0:
        #    print(nums[nums[i+1]])
        #elif nums[i]//100%10 == 1:
        #    print(nums[i+1])
        
        # this will return the outputted number instead, which might be the preferred method going forward anyways?
        if nums[i]//100%10 == 0:
            #print(nums[nums[i+1]])
            return(nums[nums[i+1]])
        elif nums[i]//100%10 == 1:
            #print(nums[i+1])
            return(nums[i+1])


        
    elif nums[i]%100 == 5:
        
        print("jump if true...")
        
        if param_1 != 0:   
            instruction_length = param_2 - i
        else:
            instruction_length = 3

    elif nums[i]%100 == 6:
        
        print("jump if false...")

        
        if param_1 == 0:   
            instruction_length = param_2 - i
        else:
            instruction_length = 3
    
    elif nums[i]%100 == 7:    
        
        print("is less than?")
            
        if param_1 < param_2:
            nums[nums[i+3]]=1
        else:
            nums[nums[i+3]]=0
        
        instruction_length = 4
        
    elif nums[i]%100 == 8:
    
        print("is equal?")
            
        if param_1 == param_2:
            nums[nums[i+3]]=1
        else:
            nums[nums[i+3]]=0   
    
    
        instruction_length = 4
        
        
        
    elif nums[i]%100 ==  99:

        print("ending...")
        #print(nums)
        #f.close()

    else:
        print("program failure")
        print(nums)
        print(f"final position: {i}")
    try:
        return(opcode(nums, i + instruction_length,input_on_load))
    except:
        print("no output generated...")
 
 
phase_settings = [0,1,2,3,4]
amps = ["a","b","c","d","e"]
_init_input = 0


#create an object type to store states of amplifiers

class amplifier:
    def __init__(self,name,nums):
        self.name = name
        self.nums = nums
    
    operate = opcode(nums,i,input_on_load)
    
    


    
def permute(lis):
    if len(lis)==0:
        return []
    if len(lis)==1:
        return [lis]
    permutations = []
    for i in range(len(lis)):
        permutation = lis[i]
        for j in permute(lis[:i]+lis[i+1:]) :
            permutations.append([permutation]+j)
           
           
    return(permutations)
    
        
        
def run_test(ordered_phases):
    msg = 0
    for amp in range(len(amps)):
        inputs = [msg,ordered_phases[amp]]
        msg = opcode(initialize(), _init_input, inputs)
    return msg
    

def amp_test():
    permutations = permute(phase_settings)
    
    outputs = []
    for permutation in permutations:
        outputs.append(run_test(permutation))
        
    print(outputs)
    


amp_test()
