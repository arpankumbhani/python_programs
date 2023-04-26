#fibonacci
def fibonacci(n):
    # Check if n is 0 or 1
    if n == 0:
        return []
    elif n == 1:
        return [0]
    
    # Create a list to store the Fibonacci sequence
    fib = [0, 1]
    
    # Generate the remaining Fibonacci numbers
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
        
    return fib

# Ask the user how many Fibonacci numbers to generate
n = int(input("How many Fibonacci numbers do you want to generate? "))

# Generate the Fibonacci sequence and print it
fib_seq = fibonacci(n)
print(fib_seq)
