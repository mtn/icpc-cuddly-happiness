numTrials = int(input())
arr = []

for i in range(0,4):
    for j in range(0,4):
        for k in range(0,4):
            temp = "4"
            if(i == 0):
                temp += " + 4"
            elif(i == 1):
                temp += " - 4"
            elif(i == 2):
                temp += " * 4"
            else:
                temp += " / 4"
            if(j == 0):
                temp += " + 4"
            elif(j == 1):
                temp += " - 4"
            elif(j == 2):
                temp +=" * 4"
            else:
                temp +=" / 4"
            if(k == 0):
                temp+=" + 4"
            elif(k == 1):
                temp +=" - 4"
            elif(k == 2):
                temp+=" * 4"
            else:
                temp+=" / 4"
            arr.append(temp)

for i in range(0,numTrials):
    num = int(input())
    found = False
    for j in range(0,64):
        if eval(arr[j]) == num:
            found = True
            break
    if(found):
        print(arr[j] + " = " + str(num))
    else:
        print "no solution"
