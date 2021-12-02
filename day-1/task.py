def gen_array_of_data():
    sweep_report = []
    with open("data.txt") as data:
        return [ int(sweep) for sweep in data.read().split("\n") ]

def increased(sweep_report):
    counter = 0
    for index in range(len(sweep_report)-1):
        if sweep_report[index] < sweep_report[index+1]:
            counter+=1
    return counter


def triple_increased(sweep_report):
    counter = 0
    three_measurement=sum(sweep_report[:3])
    for index in range(2, len(sweep_report)):
        next_three_measurement=sum(sweep_report[index-2:index+1])
        if three_measurement < next_three_measurement:
            counter+=1
        three_measurement = next_three_measurement
    return counter



data = gen_array_of_data()
print("Task1: "+str(increased(data)))
print("Task2: "+str(triple_increased(data)))