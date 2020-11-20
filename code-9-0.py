file_name = "day9.txt"
#phase_settings = [5,6,7,8,9]
#amp_names = ["a","b","c","d","e"]


#opens up the code file and returns the initial sequence of ints
def initialize():
    print("initializing integer code")
    f = open(file_name, "r")
    nums = f.read().split(',')
    
    nums = list(map(int,nums))
    
    return nums
    

    
    
class computer:
    def __init__(self, name, inputs):
        self.name = name
        self.nums = initialize()
        self.inputs = inputs
        self.outputs = []
        self.i = 0
        self.base = 0
        self.running = False
        self.waiting_for_signal = False
    
    
    def assign_value(self, value, position):
        if position<len(self.nums):
            self.nums[position]=value
        else:
            for pos in range(0,position-len(self.nums),1):
                self.nums.append(0)
            self.nums.append(value)
            
                
    
    #this function gets parameters 

    def get_params(self, param_count):
        param_list = []
        input_code = str(self.nums[self.i]).zfill(5)
        for j in range(1,param_count+1):
            if j<3:
                if   input_code[-2-j] == "1":              #immediate mode
                    try: 
                        param = self.nums[self.i+j]
                    except:
                        param = 0
                elif input_code[-2-j] == "0":              #reference position mode
                    try:
                        param = self.nums[self.nums[self.i+j]]
                    except:
                        param = 0
                elif input_code[-2-j] == "2":              #relative base mode
                    try:
                        param = self.nums[self.nums[self.i+j]+self.base]
                    except:
                        param = 0
            
            else:
                if input_code[-5] == "2":
                    param = self.base + self.nums[self.i+3]
                else:
                    param = self.nums[self.i+3]
            param_list.append(param)
        return(param_list)
    
    def opcode(self):
        code = self.nums[self.i]%100
        #code = int(str(self.nums[self.i])[-2:])
        #print(f"executing {code}")
        if code   ==1:
            #adding
            param_1,param_2,param_3 = self.get_params(3)
            
            self.assign_value(param_1 + param_2, param_3)
            
            self.i += 4
        
        elif code ==2:
            #multiplying
            param_1,param_2,param_3 = self.get_params(3)
            
            self.assign_value(param_1 * param_2, param_3)
            
            self.i += 4
            
        elif code ==3:
            #taking input
            if self.inputs != []:
                if self.nums[self.i] == 3:
                    param_1 = self.nums[self.i+1]
                if self.nums[self.i] == 103:
                    param_1 = self.i+1
                if self.nums[self.i] == 203:
                    param_1 = self.base+self.nums[self.i+1]
                self.assign_value(self.inputs.pop(0), param_1)
                self.waiting_for_signal = False
                self.i += 2
            else:
                self.waiting_for_signal = True
                self.running = False
                

        elif code ==4:
            #sending output
            param_1 = self.get_params(1)[0]
            self.outputs.append(param_1)
            self.i += 2
        elif code ==5:
            #jump if true
            param_1,param_2 = self.get_params(2)

            
            if param_1 != 0:
                self.i = param_2
            else:
                self.i += 3
                        
            
        elif code ==6:
            #jump if false
            
            param_1,param_2 = self.get_params(2)
            
            
            if param_1 == 0:
                self.i = param_2
            else:
                self.i += 3
                
        
        elif code == 7:
            #less than
            param_1,param_2,param_3 = self.get_params(3)
            
            if param_1 < param_2:
                self.assign_value(1, param_3)
            else:
                self.assign_value(0, param_3)

            
            self.i += 4
        
        elif code == 8:
            #equality test
            param_1,param_2,param_3 = self.get_params(3)
            
            if param_1 == param_2:
                self.assign_value(1, param_3)
            else:
                self.assign_value(0, param_3)
            
            self.i += 4
            
        elif code == 9:    
            #setting relative base
            param_1 = self.get_params(1)[0]
            self.base += param_1
            
            self.i += 2
        elif code == 99:
            #ending
            self.running = False
            
    #### end of computer class   ###
    
    
    
def boost_test():
    inputs = [2]
    test_comp = computer("test", inputs)
    test_comp.running = True
    while test_comp.running == True:
        test_comp.opcode()
    print(test_comp.outputs)
    
    
boost_test()
