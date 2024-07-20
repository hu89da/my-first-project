def square_even_numbers(numbers):
    # Create a new list of squares of even numbers using list comprehension
    squared_evens = [x**2 for x in numbers if x % 2 == 0]
    return squared_evens

def extract_sublist(numbers, start_index, end_index):
    # Slice the original list to extract a sublist
    sublist = numbers[start_index:end_index]
    return sublist

# Input list of integers
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Get start and end indices for sublist
start_index = int(input("Enter the start index for sublist: "))
end_index = int(input("Enter the end index for sublist: "))

# Perform operations
squared_evens = square_even_numbers(numbers)
sublist = extract_sublist(numbers, start_index, end_index)

# Display results
print("Original list:", numbers)
print("Squares of even numbers:", squared_evens)
print("Extracted sublist:", sublist)