def sort(S):
    lower = "abcdefghijklmnopqrstuvwxyz"
    s1 = []
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s2 = []
    even = "13579"
    s3 = [] 
    odd = "02468"
    s4 = []
    Ss = ""
    for i in range(len(S)):
        n = S[i]
        if n in lower:
            s1.append(n)
        if n in upper:
            s2.append(n)
        if n in even:
            s3.append(n)
        if n in odd:
            s4.append(n)
    ## sort lower letters
    for j in range(len(s1)-1):
        minIndex = j
        for k in range(j, len(s1)):
            if(lower.index(s1[k])<lower.index(s1[minIndex])):
                minIndex = k
        temp = s1[j]
        s1[j] = s1[minIndex]
        s1[minIndex] = temp
    ## sort higher letters
    for j in range(len(s2)-1):
        minIndex = j
        for k in range(j, len(s2)):
            if(upper.index(s2[k])<upper.index(s2[minIndex])):
                minIndex = k
        temp = s2[j]
        s2[j] = s2[minIndex]
        s2[minIndex] = temp
    ## sort numbers
    for j in range(len(s3)-1):
        minIndex = j
        for k in range(j, len(s3)):
            if(even.index(s3[k])<even.index(s3[minIndex])):
                minIndex = k
        temp = s3[j]
        s3[j] = s3[minIndex]
        s3[minIndex] = temp
    for j in range(len(s4)-1):
        minIndex = j
        for k in range(j, len(s4)):
            if(odd.index(s4[k])<odd.index(s4[minIndex])):
                minIndex = k
        temp = s4[j]
        s4[j] = s4[minIndex]
        s4[minIndex] = temp
    for i in range(len(s1)):
        Ss = Ss+s1[i]
    for i in range(len(s2)):
        Ss = Ss+s2[i]
    for i in range(len(s3)):
        Ss = Ss+s3[i]
    for i in range(len(s4)):
        Ss = Ss+s4[i]
    S = Ss
    print(S) 
S = input()
sort(S)

