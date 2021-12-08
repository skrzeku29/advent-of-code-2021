def gen_array_of_data():
    sweep_report = []
    with open("test-data.txt") as data:
        return data.read().split("\n")

data = gen_array_of_data()
new_data = []
oxygen = ""
co2 = ""

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

def counter_thing(data):
    for i in range(len(data[0])):
        one_counter = 0
        zero_counter = 0
        for j in range(len(data)):
            if data[j][i] == "0":
                zero_counter+=1
            else:
                one_counter+=1
        if one_counter >= zero_counter:
            # oxygen+=str(1)
            # co2+=str(0)
            new_data.append(data[i])
        else:
            oxygen+=str(0)
            co2+=str(1)

def remove_from(data, index, num):
    for i in range(len(data)):
        for j in range(len(data)):
            


print(new_data)

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