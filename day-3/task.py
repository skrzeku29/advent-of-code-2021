def gen_array_of_data():
    sweep_report = []
    with open("data.txt") as data:
        return data.read().split("\n")

data = gen_array_of_data()

gamma_rate = ""
epsilion_rate = ""

for i in range(len(data[0])):
    one_counter = 0
    zero_counter = 0
    for j in range(len(data)):
        if data[j][i] == "0":
            zero_counter+=1
        else:
            one_counter+=1
    if one_counter > zero_counter:
        gamma_rate+=str(1)
        epsilion_rate+=str(0)
    else:
        gamma_rate+=str(0)
        epsilion_rate+=str(1)

print(gamma_rate)
print(int(gamma_rate, 2))
print(epsilion_rate)
print(int(epsilion_rate, 2))
print(int(gamma_rate, 2)*int(epsilion_rate, 2))