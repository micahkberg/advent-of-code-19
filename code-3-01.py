import numpy as np

f = open("day3.txt", "r")
lis = f.read().split()
wire1_instructions = lis[0].split(",")
wire2_instructions = lis[1].split(",")

angle_dict = {
    "L": np.array([-1,0]),
    "U": np.array([0,1]),
    "R": np.array([1,0]),
    "D": np.array([0,-1])
    }
	
    
def get_positions(vector,start):
    positions = []
    leng = np.sum(vector)
    for step in range(np.sign(leng),leng + np.sign(leng),np.sign(leng)):
        mod_by = (vector * step // leng)
        positions.append(start+mod_by)
        
    return positions
	
def position_calc(instructions):
    positions = [np.array([0,0])]    
    for instruction in instructions:
        angle = angle_dict[instruction[0]]
        length = int(instruction[1:])
        new_pos_vect = angle*length
        positions = positions + get_positions(new_pos_vect,positions[-1])
    positions = positions[1:]
    return positions
    
#really slow    
#def get_intersections(positions_1,positions_2):
#    intersections = []
#    for point_1 in positions_1:
#        for point_2 in positions_2:
#            if point_1[0]==point_2[0] and point_1[1] == point_2[1]:
#                intersections.append([point_1,np.sum(point_1)])
#    return intersections
    
def get_manhatten_dist(point):
    return(abs(point[0]) + abs(point[1]))
    
    
def find_quickest_intersection(positions_1,positions_2):
    point_found = False
    total_steps = 2
    
    while point_found == False:
        print(f"searching at length {total_steps}")
        for i in range(1,total_steps):
            p1 = positions_1[i-1]
            p2 = positions_2[total_steps-i-1]
            if p1[0]==p2[0] and p1[1] == p2[1]:
                point_found = True
                print("point found!")
                quickest_intersection = p1
                break
        total_steps += 1
        
    return(quickest_intersection)
    
#find all the positions for each of the wires, uses position calc which uses get_positions
wire1_positions = position_calc(wire1_instructions)
wire2_positions = position_calc(wire2_instructions)


#print(len(wire1_positions))
#print(len(wire2_positions))
print(find_quickest_intersection(wire1_positions,wire2_positions))

#steps = 0
#for i in wire2_positions:
#    steps+=1
#    if i[0]==1002 and i[1]==68:
#        print("exists")
#        break
#for i in wire2_positions:
#    steps+=1
#    if i[0]==1002 and i[1]==68:
#        print(i)
#        print("exists")
#        break   
   
#print(steps)

#use manhatten dist to sort points
#wire1_positions.sort(key=get_manhatten_dist)
#wire2_positions.sort(key=get_manhatten_dist)

#use steps to sort points





#point_found = False

#for point_1 in wire1_positions:

#    if point_found == False:
            
#        for point_2 in wire2_positions:
#            if point_1[0] == point_2[0] and point_1[1]== point_2[1]:
#                point_found = True
#                closest_point = point_1
#                break
#    
#    else:
#        break

#print(closest_point)


#find intersections:
#intersections = get_intersections(wire1_positions,wire2_positions)
#print(intersections)

    
#testing the position generator    
#print(get_positions(np.array([-50,0]),np.array([83,90])))

