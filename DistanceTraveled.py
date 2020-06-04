#get speed and hours traveled

speed = float(input("How fast were you going?"))
while speed < 1:
    print("ERROR: Speed must be higher than zero.")
    speed = float(input("How fast were you going?"))

hours = float(input("How many hours did you travel?"))
while hours < 1:
    print("ERROR: Hours must be higher than zero.")
    hours = float(input("How many hours did you travel?"))
    
print()
print('----------------')
print('Hour\tDistance')
print('----------------')

for num in range(1, int(hours + 1)):
    distance = num*speed
    print(format(num, '.0f'), '\t', format(distance, '.0f'))

    
    
