listi = [1, 2, 3, 4, 5]
sum = 0

def listi_jami():
    global sum
    for i in listi:
        sum += i
    print(sum)

listi_jami()