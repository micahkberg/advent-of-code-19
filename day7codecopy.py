
    
        
        
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