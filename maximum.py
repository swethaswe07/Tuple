'''

 Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
'''
def min_tuple_element():
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
    
    # Calculate the minimum value using the min() function
    min_value = min(elements_tuple)
    
    # Output the minimum value
    print(min_value)

# Call the function
min_tuple_element()
