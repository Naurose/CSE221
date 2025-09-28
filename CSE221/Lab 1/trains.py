def lexicographical(name1, name2):
    for i, j in zip(name1, name2):
        if ord(j) > ord(i):
            return True
        elif ord(j) < ord(i):
            return False
        
    return len(name2) > len(name1)
 
def time(time1, time2):
    hi, mi = map(int, time1.split(":"))
    hj, mj = map(int, time2.split(":"))
    return (hj, mj) > (hi, mi)
 
n = int(input())
arr = []

for i in range(n):
    arr.append(input())
 
for i in range(1, n):
    part = arr[i].split()
    name1, time1 = part[0], part[6]
    
    for j in range(i-1, -1, -1):
        flag = False
        part = arr[j].split()
        name2, time2 = part[0], part[6]
        
        if name1 != name2:
            if lexicographical(name1, name2):
                arr[i], arr[j] = arr[j], arr[i]
                flag = True
        else:
            if time1 != time2:
                if time(time1, time2) == False:
                    arr[i], arr[j] = arr[j], arr[i]
                    flag = True
        i = i-1
        if flag == False:
            break

for i in arr:
    print(i)