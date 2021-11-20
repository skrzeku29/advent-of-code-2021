increase_counter=0
sweep_report = []
decrease_counter=0

with open("data.txt") as data:
    sweep_report = data.read().split("\n")

sweep_report = [ int(sweep) for sweep in sweep_report ]

print(str(sum(sweep_report[:3]))+" N/A")

total_index = len(sweep_report) 
three_measurement=sum(sweep_report[:3])
for index in range(2, total_index):
    next_three_measurement=sum(sweep_report[index-2:index+1])
    if three_measurement < next_three_measurement:
        print(str(next_three_measurement)+" increased")
        increase_counter+=1
    elif three_measurement >= next_three_measurement:
        print(str(next_three_measurement)+" decreased/stayed the same")
        decrease_counter+=1
    three_measurement = next_three_measurement


print("Total amount increased: "+str(increase_counter))
print("Total amount decreased or stayed the same: "+str(decrease_counter))