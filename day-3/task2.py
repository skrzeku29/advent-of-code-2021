def gen_array_of_data():
    sweep_report = []
    with open("data.txt") as data:
        return data.read().split("\n")

data = gen_array_of_data()
# new_data = []
# oxygen = ""
# co2 = ""

# def reverse_array(data):
#     # new_array=[[]]
#     new_array=[[0]*5]*(len(data)-1)
#     for i in range(5):
#         for item in data:
#             new_array[i].append(item)
        
#     return new_array

# for i in range(len(data[0])):
#     one_counter = 0
#     zero_counter = 0
#     for j in range(len(data)):
#         if data[j][i] == "0":
#             zero_counter+=1
#         else:
#             one_counter+=1
#     if one_counter >= zero_counter:
#         # oxygen+=str(1)
#         # co2+=str(0)
#         new_data.append(data[i])
#     else:
#         oxygen+=str(0)
#         co2+=str(1)
def counter_thing(p_data):
    total=""
    oxygen = ""
    co2 = ""
    data = p_data
    bit=0
    binary=0
    data_limit=len(data)
    data2_limit=len(data[0])
    # print("index_assign: "+str(bit))

    for binary in range(data_limit):
        one_counter = 0
        zero_counter = 0
        bit=0
        # print(binary)
        # print(bit)
        # print(data)
        # print(data[binary][bit])
        # for i in range(5):
        #     print(data[i])
        while bit < data2_limit:
            if data[binary][bit] == "0":
                zero_counter+=1
            else:
                one_counter+=1
            bit+=1
        if one_counter >= zero_counter:
            oxygen+=str(1)
            co2+=str(0)
            total+=str(1)
            # print("index: "+str(bit))
            data = remove_from(data, 0, binary)
            data2_limit = len(data[0])
            # print(data)
        elif zero_counter > one_counter:
            co2+=str(1)
            oxygen+=str(0)
            total+=str(0)
            # print("index: "+str(bit))
            data = remove_from(data, 1, binary)
            data2_limit = len(data[0])
        
    # print(data)
        # print(one_counter)
        # print(zero_counter)
        # print("next")

        # print(data)
        # print(oxygen)
        # print(co2)

    # print(oxygen)
    # print(co2)
    # print(total)
    return oxygen

def opposite_counter_thing(p_data):
    total=""
    oxygen = ""
    co2 = ""
    data = p_data
    bit=0
    binary=0
    data_limit=len(data)
    data2_limit=len(data[0])
    # print("index_assign: "+str(bit))

    for binary in range(data_limit):
        one_counter = 0
        zero_counter = 0
        bit=0
        # print(binary)
        # print(bit)
        # print(data)
        # print(data[binary][bit])
        # for i in range(5):
        #     print(data[i])
        while bit < data2_limit:
            if data[binary][bit] == "0":
                zero_counter+=1
            elif len(data[0]) == 0:
                one_counter=1000
            elif len(data[0]) == 1:
                zero_counter=1000
                for j in range(len(data)):
                    data[j].pop(0)
            else:
                one_counter+=1
            bit+=1
        if one_counter >= zero_counter:
            oxygen+=str(1)
            co2+=str(0)
            total+=str(1)
            # print("index: "+str(bit))
            data = remove_from(data, 1, binary)
            data2_limit = len(data[0])
            # print(data)
        elif zero_counter > one_counter:
            co2+=str(1)
            oxygen+=str(0)
            total+=str(0)
            # print("index: "+str(bit))
            data = remove_from(data, 0, binary)
            data2_limit = len(data[0])
        
    # print(data)
        # print(one_counter)
        # print(zero_counter)
        # print("next")

        # print(data)
        # print(oxygen)
        # print(co2)

    # print(oxygen)
    # print(co2)
    return co2


def remove_from(data, num, index):
    # print("removing")
    # print(data)
    # for i in range(5):
    #     print(data[i][index])
    # print(len(data[0]))
    size = len(data[0])
    i=0
    while i < size:
        # print("i "+str(i)+" size "+str(size))
        # print(data[i][index])
        # print(data)
        # print(i)
        # print(len(data[index]))
        if data[index][i] == str(num):
            # print("Deleting")
            # print(data[index][i])
            for j in range(len(data)):
                data[j].pop(i)
            size = len(data[index])
        # print(size)
        else:
            i+=1
            # del data[i][index]
        # data[i].pop(index)
        # print(i)
        # print(data)
    # print(data)
    # for i in range(5):
    #     print(data[i][index])

    return data
        
            
# print(data)
flipp=list(map(list, zip(*data)))
print(flipp)
nd_data=flipp

# print("oxygen "+str(counter_thing(flipp)))

print("co2 "+str(opposite_counter_thing(nd_data)))

# 10111
# 01010
# print(int('10111', 2) * int('01010', 2) )



# 011111101111 100000111000
print(int('011111101111', 2) * int('100000111000', 2) )




# print(flipp)

# for i in range(len(data[0])):
#     one_counter = 0
#     zero_counter = 0
#     for j in range(len(data)):
#         if data[j][i] == "0":
#             zero_counter+=1
#         else:
#             one_counter+=1
#     if one_counter >= zero_counter:
#         oxygen+=str(1)
#         co2+=str(0)
#     else:
#         oxygen+=str(0)
#         co2+=str(1)

# print(oxygen)
# print(int(oxygen, 2))
# print(co2)
# print(int(co2, 2))
# print(int(oxygen, 2)*int(co2, 2))