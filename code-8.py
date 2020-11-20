fname = "day8.txt"
f = open(fname, "r")
img_raw = f.read().strip()
size_w_h = [25,6]
import numpy as np


def make_layer(img):
    new_layer=[]
    for h in range(size_w_h[1]):
        new_row = img[:size_w_h[0]]
        img = img[size_w_h[0]:]
        new_layer.append(new_row)
        #print(new_layer)
    return(new_layer, img)
    
    
def process_img(img):
    layered_img = []
    while len(img) >= 25*6:
        new_layer, img = make_layer(img)
        layered_img.append(new_layer)
    return layered_img
    
    
layered_img = np.array(process_img(img_raw))

def char_counter(img,char):
    counts = []
    for layer in layered_img:
        count = 0
        for line in layer:
            count += line.count(char)
        counts.append(count)
    return(counts)
    
#counting_lis = []
#for i in [0,1,2]:
#    counting_lis.append(char_counter(layered_img,str(i)))

      
#mini = min(counting_lis[0])
#target_layer = counting_lis[0].index(mini)
#print(counting_lis[1][target_layer]*counting_lis[2][target_layer])

#print("img layer length")
#print(len(layered_img))
print(layered_img[0][0][0])
img = ""
for y in range(6):
    new_row = ""
    for x in range(25):
        layer = 0
        while True:
            new_pixel = layered_img[layer][y][x]
            if new_pixel != "2" or layer==len(layered_img):
                break
            else:   
                layer+=1    
        if new_pixel=="0":
            new_pixel = " "
        new_row = new_row + new_pixel      
    img = img + new_row + "\n"


print(img)
                