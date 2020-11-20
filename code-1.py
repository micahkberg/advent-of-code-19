f = open("day1.txt", "r")
nums = f.read().split()


def fuel_check(mass):
    fuel = mass//3 - 2
    #print("fuel at "+str(fuel))
    if fuel < 0:
        fuel = 0
        return(fuel)
    else:
        fuel+=fuel_check(fuel)
        return(fuel)
  
total_fuel = 0

for i in nums:
    total_fuel += fuel_check(int(i))
    print("module mass: " + i + "   fuel totaled: " + str(total_fuel))

print(total_fuel)

#print(fuel_check(14))
#print(fuel_check(1969))
#print(fuel_check(100756))
