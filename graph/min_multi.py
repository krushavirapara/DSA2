def min_multiplications(start, end, multipliers):
    MOD = 10**5  # Since numbers are taken modulo 100000
   

    def backtrack(i,start, steps):
        # Base Case: If we reach the end, return steps
        if start == end:
            return steps
        
        # If already visited with fewer steps, prune the recursion
      

         # Store the minimum steps required for this value

        min_steps = float('inf')

        # Try multiplying with each number in multipliers
        for idx  in range(i,len(multipliers)):
            new_val = (start * multipliers[idx]) % MOD
            if new_val>end:
                break
            min_steps = min(min_steps, backtrack(i,new_val, steps + 1))

        return min_steps

    result = backtrack(0,start, 0)
    return result if result != float('inf') else -1

# Example Usage
start = 5
end = 125
multipliers = [2, 3, 5]

print(min_multiplications(start, end, multipliers))  # Output: Minimum number of steps
