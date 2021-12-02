def gen_array_of_data():
    sweep_report = []
    with open("data.txt") as data:
        return data.read().split("\n")

def calculate_position(data):
    horiz=0
    depth=0
    for item in data:
        item = item.split(" ")
        if item[0] == "forward":
            horiz+=int(item[1])
        elif item[0] == "up":
            depth-=int(item[1])
        elif item[0] == "down":
            depth+=int(item[1])
    return horiz*depth

def calculate_position_with_aim(data):
    horiz=0
    depth=0
    aim=0
    for item in data:
        item = item.split(" ")
        if item[0] == "forward":
            horiz+=int(item[1])
            tmp_aim=aim
            if aim != 0:
                if aim < 0:
                    tmp_aim=abs(tmp_aim)
                depth+=(int(item[1])*tmp_aim)
        elif item[0] == "up":
            aim-=int(item[1])
        elif item[0] == "down":
            aim+=int(item[1])
    return horiz*depth
        
data = gen_array_of_data()

print("task1: "+str(calculate_position(data)))
print("task2: "+str(calculate_position_with_aim(data)))