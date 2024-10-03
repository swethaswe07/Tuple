'''
Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
'''

def count_tuple_value():
    # Input the tuple elements
    elements = input("Enter the tuple elements (space-separated): ").split()
    
    # Convert the input strings to a tuple of integers
    elements_tuple = tuple(int(num) for num in elements)
    
    # Input the value to count
    value_to_count = int(input("Enter the value to count: "))
    
    # Count the occurrences of the value in the tuple
    count = elements_tuple.count(value_to_count)
    
    # Output the count
    print(count)

# Call the function
count_tuple_value()
