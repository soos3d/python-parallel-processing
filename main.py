import time

def fibonacci(n):
    """Calculate the nth Fibonacci number using an iterative method."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def compute_sum_of_fibonacci(data):
    """Calculate the sum of Fibonacci numbers for a list of numbers."""
    return sum(fibonacci(i) for i in data)

if __name__ == "__main__":
    print('Running a sequential process...')
    # Initialize the data (list of numbers)
    data = list(range(1, 10001))
    
    # Start timing
    start_time = time.time()
    
    # Calculate the sum of Fibonacci numbers using a sequential process
    result = compute_sum_of_fibonacci(data)
    
    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Print the total sum and elapsed time
    print(f"Sum of Fibonacci Numbers: {str(result)[:5]}...")
    print(f"Elapsed Time: {elapsed_time:.4f} seconds")
