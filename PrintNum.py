'''
Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
'''
def count_tuple_elements():
    # Input the tuple elements
    elements = input("Enter the tuple elements (space-separated): ").split()
    
    # Convert the input strings to a tuple
    elements_tuple = tuple(elements)
    
    # Get the number of elements in the tuple
    num_elements = len(elements_tuple)
    
    # Output the number of elements
    print(num_elements)

# Call the function
count_tuple_elements()
