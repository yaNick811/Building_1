class Building_1:
    Total = 0

    def __init__(self):
        Building_1.Total += 1

for i  in range(40):
    building = Building_1()
    print(Building_1.Total)