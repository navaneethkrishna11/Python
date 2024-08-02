def substring(items):
    sub=[]

    for string in items:
        length=len(string)
        for start in range(length):
            for end in range(start+1,length+1):
                sub.append(string[start:end])

    return sub

i=input("string : ")
items=[]
items.append(i)
print(substring(items))
