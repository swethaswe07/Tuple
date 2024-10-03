'''
 Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60

'''

def sum_tuple_elements():
    # Input the tuple elements
    elements = input("Enter the tuple elements (space-separated): ").split()
    
    # Convert the input strings to integers and store in a tuple
    elements_tuple = tuple(int(num) for num in elements)
    
    # Initialize a variable to hold the sum
    total_sum = 0
    
    # Calculate the sum without using the sum() method
    for num in elements_tuple:
        total_sum += num
    
    # Output the total sum
    print(total_sum)

# Call the function
sum_tuple_elements()
