increase_counter=0
sweep_report = []
decrease_counter=0

with open("data.txt") as data:
    sweep_report = data.read().split("\n")

print(str(sweep_report[0])+" N/A")
for index in range(len(sweep_report)-1):
    if int(sweep_report[index]) < int(sweep_report[index+1]):
        print(str(sweep_report[index+1])+" increased")
        increase_counter+=1
    if int(sweep_report[index]) >= int(sweep_report[index+1]):
        print(str(sweep_report[index+1])+" decreased/stayed same")
        decrease_counter+=1

print("Total amount increased: "+str(increase_counter))
print("Total amount decreased or stayed the same: "+str(decrease_counter))