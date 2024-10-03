'''
Raju is a 3rd grade kid, he is struggling to find which is "even" number and which is a "odd" number. So, his teacher gave him a task to find how many even numbers and how many odd numbers are there in the given collection of values and print "Even" if even count is more than odd count, else print "Odd", if odd count is more and print "Equal" if both even count and odd count are same. Help Raju to understand the difference of even and odd.
Sample Input:
1 2 3 4 5
Sample Output:
Odd
'''

def count_even_odd():
    # Input the values as a space-separated string
    values = input("Enter the numbers (space-separated): ").split()
    
    # Initialize counters for even and odd numbers
    even_count = 0
    odd_count = 0
    
    # Iterate through each value to count even and odd numbers
    for value in values:
        num = int(value)
        if num % 2 == 0:
            even_count += 1  # Increment even count
        else:
            odd_count += 1   # Increment odd count
    
    # Determine which count is greater
    if even_count > odd_count:
        print("Even")
    elif odd_count > even_count:
        print("Odd")
    else:
        print("Equal")

# Call the function
count_even_odd()
