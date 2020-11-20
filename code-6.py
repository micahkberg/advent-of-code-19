import numpy as np
#prepare the input list

f = open("day6.txt", "r")
orbit_lis = f.read().split()

def orbsplit(string):
    return string.split(")")

orbit_lis = np.array(list(map(orbsplit, orbit_lis)))

#print(orbit_lis)



def counting_thru_list(lis):
    counter = 0
    for pair in lis:
        #print(pair)
        parent_lis = np.array([pair[0]])
        child = pair[1]
        #print(f"list of parents is: {parent_lis}")
        while parent_lis[-1] != "COM":
            new_parent_index = np.where(lis[:,1] == parent_lis[-1])[0][0]
            new_parent = lis[new_parent_index,0]
            parent_lis = np.append(parent_lis, new_parent)
        
        
        counter += parent_lis.size
          
        
        
    

    return(counter)
   
print("begin test")
#print(counting_thru_list(orbit_lis))



def make_com_tree(lis,loc_ind):
    tree = [lis[loc_ind,0]]
    
    while tree[-1] != "COM":
        new_parent_index = np.where(lis[:,1] == tree[-1])[0][0]
        new_parent = lis[new_parent_index,0]
        tree.append(new_parent)
    return tree
    
    
def make_path(tree1,tree2):
    while tree1[-1] == tree2[-1] and tree1[-2] == tree2[-2]:    
        del tree1[-1]
        del tree2[-1]
        
    del tree1[-1]
    return tree1+tree2
        
        
def path_to_SAN(lis):
    you_index = np.where(lis[:,1] == "YOU")[0][0]
    you_tree = make_com_tree(lis,you_index)
    
    san_index = np.where(lis[:,1] == "SAN")[0][0]
    san_tree = make_com_tree(lis,san_index)
    path = make_path(you_tree, san_tree)
    print(path)
    print(len(path))
    
    
    

path_to_SAN(orbit_lis)
    
    

