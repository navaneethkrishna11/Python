"""
There is a jar full of candies for sale at a mall counter. The jar has the capacity N that is JAR can contain 
maximum N Candies when a JAR is full. At any point in time, JAR can have an M number of candies where 
M<=N. Candies are served to the customers. JAR is never remaining empty as when the last K candidates are 
left, JAR is refilled with new candidates in such a way that JAR gets full. Write the code to implement the 
above scenario. Display JAR at the counter with the available number of candies.
Input should be the number of candies one customer orders at a point in time. Update the JAR after every 
purchase and display JAR at the counter. The output should give the number of candies sold and the updated 
number of candies in the JAR. If the input is more than the number of candies in JAR, return “INVALID INPUT”.
Given,
N=10, Where N is the number of candies available, K<=5, Where K is the number of minimum candies that 
must be inside JAR ever.
Example1: (N=10,K=<5)
Input #1:
3
Output :
Number of Candies Sold: 3
Number of Candies available:7
"""
def sell_candies(candies_ordered):
    global jar_candies, N, K

    if candies_ordered > jar_candies:
        print("INVALID INPUT")
        return

    jar_candies -= candies_ordered

    if jar_candies <= K:
        jar_candies = N

    print(f"Number of Candies Sold: {candies_ordered}")
    print(f"Number of Candies available: {jar_candies}")


# Initialize the jar
N = 10  # Maximum capacity of the jar
K = 5  # Minimum number of candies that should trigger a refill
jar_candies = N  # Initial number of candies

# Example inputs
sell_candies(3)  # Expected output: 3 candies sold, 7 remaining
sell_candies(5)  # Expected output: 5 candies sold, 10 remaining (refilled)
sell_candies(12)  # Expected output: INVALID INPUT



"""
Write a Python program that generates a random number between a user-defined lower limit and a user-defined upper limit. The program should then prompt the user to guess the number, providing hints ("Low" or "High") if the user's guess is not correct. The program should continue to prompt the user until they correctly guess the number, and then display the total number of guesses made.

Constraints:

The program should use the random module to generate the random number.
The program should use a while loop to repeatedly prompt the user for guesses until they correctly guess the number.
The program should display a hint ("Low" or "High") after each incorrect guess.
The program should display the total number of guesses made after the user correctly guesses the number.

Example Input/Output:

User enters lower limit: 1
User enters upper limit: 10
Program generates random number: 7
User guesses: 5
Program responds: "High"
User guesses: 8
Program responds: "Low"
User guesses: 7
Program responds: "You guessed it right!"
Program displays: "Total number of guesses: 3
"""
import random as rd

lower=int(input("enter the lower limit : "))
upper=int(input("enter the upper limit :  "))
count = 0
state=True

b=rd.randint(lower,upper)
while state:
    a = int(input("enter a guess : "))
    count +=1
    if a == b:
        print("You Guessed it right")
        state=False
    elif a<b :
     print('High')
     count=count+1

    elif a>b :
     print('Low')
     count=count+1

print("Total number of guess : ",count)

"""
Rock paper scissors
"""


