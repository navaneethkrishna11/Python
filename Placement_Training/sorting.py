def sort(s):
    l=list(s)
    n=len(l)

    for i in range(n):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

    sorted_string="".join(l)
    return sorted_string

s="kerala"
sg=sort(s)
print(sg)
