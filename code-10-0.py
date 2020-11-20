import numpy as np

def get_grid():
    file_name = "day10.txt"
    f = open(file_name, "r")
    grid = np.array(f.read().split())
    return(grid)


def asteroid_positions():
    h,w = grid.shape[0],len(grid[0])
    position_lis=[]
    for x in range(w):
        for y in range(h):
            if grid[y][x] == "#":
                position_lis.append([x,y])
    return(position_lis)
    
    
def count_visible_objects(position):
    vectors = []
    for asteroid in positions:
        vector = np.array(asteroid) - np.array(position)
        v_len = np.sqrt(vector[0]**2 + vector[1]**2)
        if v_len != 0:
            vector = vector/v_len
        vector = [round(vector[0],5),round(vector[1],5)]
        if vector in vectors or v_len == 0:
            pass
        else:
            vectors.append(vector)
        
    return(len(vectors))
    
    
def print_count_map(results):
    h,w = grid.shape[0], len(grid[0])
    output = ""
    for y in range(h):
        for x in range(w):
            obj = grid[y][x]
            if obj==".":
                output+="."
            else:
                searching = True
                while searching ==True:
                    for result in results:
                        if result[1]==[x,y]:
                            output+=str(result[0])
                            searching=False
                            break
        output+="\n"            
    return(output)            
    



grid=get_grid()
positions = asteroid_positions()  
def find_all_sightlines():
    results = []
    for asteroid in positions:
        count = count_visible_objects(asteroid)
        results.append([count,asteroid])
    return(results)

def find_best_position(results):
    maximum = 0
    for result in results:
        if result[0]>maximum:
            maximum = result[0]
            best_loc = result[1]
    print(f"maximum visible asteroids is {maximum} from cooridnates {best_loc}")        

results = find_all_sightlines()
find_best_position(results)
#print(print_count_map(results))        
        