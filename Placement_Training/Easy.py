"""
There are total n number of Monkeys sitting on the branches of a huge Tree. As travelers offer Bananas and Peanuts, the Monkeys jump down the Tree. If every Monkey can eat k Bananas and j Peanuts. If total m number of Bananas and p number of Peanuts are offered by travelers, calculate how many Monkeys remain on the Tree after some of them jumped down to eat.
At a time one Monkeys gets down and finishes eating and go to the other side of the road. The Monkey who climbed down does not climb up again after eating until the other Monkeys finish eating.
Monkey can either eat k Bananas or j Peanuts. If for last Monkey there are less than k Bananas left on the ground or less than j Peanuts left on the ground, only that Monkey can eat Bananas(<k) along with the Peanuts(<j).
Write code to take inputs as n, m, p, k, j and return  the number of Monkeys left on the Tree.
    Where, n= Total no of Monkeys
        k= Number of eatable Bananas by Single Monkey (Monkey that jumped down last may get less than k Bananas)
        j = Number of eatable Peanuts by single Monkey(Monkey that jumped down last may get less than j Peanuts)
        m = Total number of Bananas
        p  = Total number of Peanuts
Remember that the Monkeys always eat Bananas and Peanuts, so there is no possibility of k and j having a value zero

Example 1:
Input Values    
20
2
3
12
12

Output Values
Number of  Monkeys left on the tree:10
Note: Kindly follow  the order of inputs as n,k,j,m,p as given in the above example. And output must include  the same format  as in above example(Number of Monkeys left on the Tree:)
For any wrong input display INVALID INPUT
"""
#Output
#---------
n=int(input("enter total number of monkeys : "))
k=int(input("enter the number of eatable Bananas : "))
j=int(input("enter the number of eatable Peanuts : "))
m=int(input("Total number of Bananas :  "))
p=int(input("Total number of Peanuts : "))
count=0
for i in range(n):
 if m>k :
    count=count+1
    m=m-k
 elif p>j:
     count=count+1
     p=p-j
 elif k>m and j>p:
    count=count+1
    m=m-k
    p=p-j

print(count)
print("Number of monkeys left on the tree : ",n-count)


"""
Jack and Jill are playing a string game. Jack has given Jill two strings A and B. Jill has to derive a string C from  
A, by deleting elements from string A, such that string C does not contain any element of string B. Jill needs  
help to do this task. She wants a program to do this as she is lazy. Given strings A and B as input, give string C  
as Output. 
Example 1: 
Input: 
tiger -> input string A 
ti -> input string B 
Output: 
ger -> Output string C 
 
Example 2: 
Input: 
processed -> input string A 
esd -> input string B 
Output: 
proc -> Output string C 
 
Example 3: 
Input: 
talent -> input string A 
tens -> input string B 
Output: 
al -> Output string C
"""
#output
#-----------
a=input("enter a string A : ")
b=input("enter a string B: ")
st=''
for i in a:
    if i not in b:
        st +=i

print(st)
