goal_output = 19690720


def initialize(noun,verb):
    f = open("day2.txt", "r")
    nums = f.read().split(',')
    #print("code recieved: " + str(nums))
    #print("updating code...")
    nums = list(map(int,nums))
    nums[1] = noun
    nums[2] = verb
    return nums
    
  
def opcode(nums, i):
    if nums[i] ==1:
        #print("adding...")
        nums[nums[i+3]] = nums[nums[i+1]]+nums[nums[i+2]]
        #print(nums)
        i+=4
        opcode(nums, i)
    elif nums[i] ==2:
        #print("multiplying...")
        nums[nums[i+3]] = nums[nums[i+1]]*nums[nums[i+2]]
        #print(nums)
        i+=4
        opcode(nums, i)
    elif nums[i] ==99:
        print("ending...")
        #print(nums)
        #f.close()
    return(nums[0])
        
def search():
    for noun in range(0,100):
        for verb in range(0,100):
            nums = initialize(noun, verb)
            output = opcode(nums, 0)
            print(output)
            if output == goal_output:
                print("noun: " + str(noun) + "   verb: " + str(verb))
                print("checkvalue: " + str(100*noun +verb))
                return(output)

                
print(search())