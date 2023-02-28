import random

def calculate_payback(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return 20
    elif a == 1 and b == 1 and c == 1:
        return 15
    elif a == 2 and b == 2 and c == 2:
        return 5
    elif a == 3 and b == 3 and c == 3:
        return 3
    elif a == 3 and b == 3:
        return 2
    elif a == 3:
        return 1
    else:
        return 0

def timeToGamble():
    coins = 10
    slotsPulled = 0

    while coins > 0:
        slotsPulled += 1
        slot1 = random.randint(0, 3)
        slot2 = random.randint(0, 3)
        slot3 = random.randint(0, 3)
        coins += (calculate_payback(slot1, slot2, slot3) - 1)

    return slotsPulled

if __name__ == '__main__':

    totalPulls = []
    sum = 0
    runs = 10000
    for i in range(runs):
        result = timeToGamble()
        totalPulls.append(result)
        sum += result
    print(sum / runs)
    print(totalPulls)
    totalPulls.sort()
    print(totalPulls[int(runs/2)])
