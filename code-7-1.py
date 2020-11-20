file_name = "day7.txt"
phase_settings = [5,6,7,8,9]
amp_names = ["a","b","c","d","e"]


#makes permutations of the phase settings
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

#opens up the code file and returns the initial sequence of ints
def initialize():
    f = open(file_name, "r")
    nums = f.read().split(',')
    
    nums = list(map(int,nums))
    
    return nums
    
#this function gets parameters when given the number list, the current position, and how many parameters to get
def get_params(param_count, i , nums):
    param_list = []
    input_code = str(nums[i]).zfill(4)
    for j in range(1,param_count+1):
        if j<3:
            if input_code[-2-j] == "1":
                param = nums[i+j]
            elif input_code[-2-j] == "0":
                param = nums[nums[i+j]]
        else:
            param = nums[i+3]
        param_list.append(param)
    return(param_list)
    
    
class computer:
    def __init__(self, name, inputs):
        self.name = name
        self.nums = initialize()
        self.inputs = inputs
        self.outputs = []
        self.i = 0
        self.running = False
        self.waiting_for_signal = False
    
    
    
    
    def opcode(self):
        code = str(self.nums[self.i])[-1]
        if code   =="1":
            #adding
            param_1,param_2,param_3 = get_params(3, self.i, self.nums)
            
            self.nums[param_3] = param_1 + param_2
            
            self.i += 4
        
        elif code =="2":
            #multiplying
            param_1,param_2,param_3 = get_params(3, self.i, self.nums)
            
            self.nums[param_3] = param_1 * param_2
            
            self.i += 4
            
        elif code =="3":
            #taking input
            if self.inputs != []:
                self.nums[self.nums[self.i+1]] = self.inputs.pop(0)
                self.waiting_for_signal = False
                self.i += 2
            else:
                self.waiting_for_signal = True
                self.running = False
                

        elif code =="4":
            #sending output
            self.outputs.append(self.nums[self.nums[self.i+1]])
            self.i += 2
        elif code =="5":
            #jump if true
            param_1 = get_params(1, self.i, self.nums)[0]
            param_2 = self.nums[self.i+2]
            
            if param_1 != 0:
                self.i = self.nums[param_2]
            else:
                self.i += 3
                        
            
        elif code =="6":
            #jump if false
            
            param_1 = get_params(1, self.i, self.nums)[0]
            param_2 = self.nums[self.i+2]
            
            if param_1 == 0:
                self.i = param_2
            else:
                self.i += 3
                
        
        elif code =="7":
            #less than
            param_1,param_2,param_3 = get_params(3, self.i, self.nums)
            
            if param_1 < param_2:
                self.nums[param_3] = 1
            else:
                self.nums[param_3] = 0
            
            self.i += 4
        
        elif code =="8":
            #equality test
            param_1,param_2,param_3 = get_params(3, self.i. self.nums)
            
            if param_1 == param_2:
                self.nums[param_3] = 1
            else:
                self.nums[param_3] = 0
            
            self.i += 4
            
            
        elif code =="9":
            #ending
            self.running = False
            
    #### end of computer class   ###
    
    
#generates a dictionary where the amps listed are all instanced
def make_amps(phasePermutation):
    amps = {name: computer(name = name, inputs = []) for name in amp_names}
    i = 0
    for amp in amps:
        amps[amp].inputs.append(phasePermutation[i])
        i+=1
    return(amps)
    
def run_amp_sequence(amps):
    i=0
    while i < 5:
        amp = amp_names[i]
        #print(f"exucting code on amp {amps[amp].name}")
        
        amps[amp].running = True
        while amps[amp].running == True:
            amps[amp].opcode()
        
        if amps[amp].name=="e" and amps[amp].waiting_for_signal == False:
            return(amps[amp].outputs.pop(0))
        elif amps[amp].name=="e" and amps[amp].waiting_for_signal == True:
            amps["a"].inputs.append(amps["e"].outputs.pop(0))
            i=0
        else:
            #print(amps[amp].outputs)
            amps[amp_names[i+1]].inputs.append(amps[amp].outputs.pop(0))
            i+=1
    

def generate_output_space(phasePermutations):
    results = []
    for phasePermutation in phasePermutations:
        print(f"testing permutation: {phasePermutation}")
        amps = make_amps(phasePermutation)
        amps["a"].inputs.append(0)
        result = run_amp_sequence(amps)
        results.append(result)
    return(results)
    
def experiment_main():
    phasePermutations = permute(phase_settings)
    results = generate_output_space(phasePermutations)
    maximum = max(results)
    best_arrangement = phasePermutations[results.index(maximum)]
    print(f"found highest output of: {maximum}")
    print(f"best arrangement is: {best_arrangement}")


experiment_main()