'''
Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30

'''

def max_tuple_element():
    # Input the number of elements
    n = int(input("Enter the number of elements: "))
    
    # Initialize an empty list to collect the elements
    elements = []
    
    # Input each element in separate lines
    for _ in range(n):
        element = int(input())
        elements.append(element)
    
    # Convert the list to a tuple
    elements_tuple = tuple(elements)
    
    # Calculate the maximum value using the max() function
    max_value = max(elements_tuple)
    
    # Output the maximum value
    print(max_value)

# Call the function
max_tuple_element()
