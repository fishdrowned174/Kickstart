alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Z", "Y", "Z"]

for i in range(len(code)):
    j = i + 1
    k = i + 2
    for i in range(len(alpha) - 3):
        l1 = alpha[i]
        l2 = alpha[i + 1]
        l3 = alpha[i + 2]
        # print(l1)
        if code[l1] == code[l2] == code[l3]:
            print(l1, l2, l3)
            times = times + 1
    
print(times)
