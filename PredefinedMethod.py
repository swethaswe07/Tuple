'''
 Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60

'''
def sum_tuple_elements():
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
    
    # Calculate the sum using the sum() function
    total_sum = sum(elements_tuple)
    
    # Output the sum
    print(total_sum)

# Call the function
sum_tuple_elements()
