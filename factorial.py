'''
Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6

'''
def factorial(n):
    # Function to calculate factorial without using factorial() method
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def count_and_factorial():
    # Input the tuple elements
    elements = input("Enter the tuple elements (space-separated): ").split()
    
    # Convert the input strings to a tuple of integers
    elements_tuple = tuple(int(num) for num in elements)
    
    # Input the value to count
    value_to_count = int(input("Enter the value to count: "))
    
    # Count the occurrences of the value in the tuple
    count = elements_tuple.count(value_to_count)
    
    # Calculate the factorial of the count
    fact_value = factorial(count)
    
    # Output the factorial value
    print(fact_value)

# Call the function
count_and_factorial()
