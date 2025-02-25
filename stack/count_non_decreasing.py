#https://www.geeksforgeeks.org/count-natural-numbers-whose-permutation-greater-number/
#backtracking
def helper(n, v, start, count, num):
    if n == 0:
        return
    
    for i in range(start, 10):
        v.append(str(i))
        if int("".join(v)) <= num:
            count[0] += 1
            helper(n - 1, v, i, count, num)  # Continue with i to ensure non-decreasing order
        v.pop()

def count_non_decreasing_numbers(num):
    count = [0]  # Use a list to hold count to update it within helper
    max_digits = len(str(num))  # Maximum number of digits in num

     # Consider numbers with 1 to max_digits
    helper(max_digits, [], 1, count, num)

    return count[0]

# Example usage:
num = 100
print(f"Count of non-decreasing numbers less than or equal to {num}: {count_non_decreasing_numbers(num)}")

        
        