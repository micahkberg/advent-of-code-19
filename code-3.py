import numpy as np

f = open("day3.txt", "r")
lis = f.read().split()
wire1 = lis[0].split(",")
wire2 = lis[1].split(",")



angle_dict = {
    "L": np.array([-1,0]),
    "U": np.array([0,1]),
    "R": np.array([1,0]),
    "D": np.array([0,-1])
    }
    

def position_calc(instructions):
    positions = [np.array([0,0])]    
    for instruction in instructions:
        angle = angle_dict[instruction[0]]
        length = int(instruction[1:])
        new_pos_vect = angle*length
        positions.append(positions[-1]+new_pos_vect)
    
    return positions

def check_perpendicularity(seg1,seg2):
    vec1 = seg1[0]-seg1[1]
    print(vec1)
    vec2 = seg2[0]-seg2[1]
    print(vec2)
    addend = vec1+vec2
    print(addend)
    if addend[0] !=0 and addend[1] != 0:
        return(True)
    else:
        return(False)


def check_intersect(line1,line2):
    #print("testing")
    
    if check_perpendicularity(line1,line2):
        
        
    else:
        check_overlap
    
    try:
        if line1[0][0] in range(line2[0][0],line2[1][0]+1,(line2[0][0]-line2[1][0])//abs(line2[0][0]-line2[1][0])):
            if line2[0][1] in range(line1[0][1],line1[1][1]+1,(line1[0][1]-line1[1][1])//abs(line1[0][1]-line1[1][1])):
                intersection = [line1[0][0],line2[0][1]]
                return intersection
    except:
        try:
            if line2[0][0] in range(line1[0][0],line1[1][0]+1,(line1[0][0]-line1[1][0])//abs(line1[0][0]-line1[1][0])):
                if line1[0][1] in range(line2[0][1],line2[1][1]+1,(line2[0][1]-line2[1][1])//abs(line2[0][1]-line2[1][1])):
                    intersection = [line2[0][0],line1[0][1]]
                    return intersection
        except:
            #print("exception")
            raise Exception("doesn't intersect")

def compare_segments(lis1, lis2):
    intersections = []
    for seg_num_1 in range(len(lis1)-1):
        end_points_1 = [lis1[seg_num_1],lis1[seg_num_1+1]]
        for seg_num_2 in range(len(lis2)-1):
            end_points_2 = [lis2[seg_num_2],lis2[seg_num_2+1]]
            #print("testing...")
            try: 
                #print("test")
                out = check_intersect(end_points_1,end_points_2)
                #print("intersection!")
                intersections.append(out)
                #yay an answer if we are here
            except:
                break

def closest_intersections(intersections):
    shortest = [[0,0],10000000000000000000000000]
    for intersection in intersections:
        length = intersection[0]+intersection[1]
        if length>shortest[2]:
            shortest=[intersection,length]
    return shortest


test_seg1 = np.array([[1,100],[100,100]])
test_seg2 = np.array([[50,50],[75,50]])
test_seg3 = np.array([[100,60],[100,-60]])

###print("checking perpendicular...")
###print(check_perpendicularity(test_seg1,test_seg2))
###print(check_perpendicularity(test_seg1,test_seg3))


wire1_positions = position_calc(wire1)
wire2_positions = position_calc(wire2)
#print(wire1_positions)
#print(wire2_positions)
intersections = compare_segments(wire1_positions,wire2_positions)
print(intersections)
print(check_intersect([[10,10],[20,10]],[[15,15],[-15,15]]))
print(closest_intersections(intersections))