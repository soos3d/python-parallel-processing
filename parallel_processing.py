from mpi4py import MPI
import time

def fibonacci(n):
    """Calculate the nth Fibonacci number using an iterative method."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def compute_partial_sum_of_fibonacci(data):
    """Calculate the partial sum of Fibonacci numbers for a list of numbers."""
    return sum(fibonacci(i) for i in data)

if __name__ == "__main__":
    
    # Start timing
    start_time = time.time()
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Initialize the data (list of numbers)
    if rank == 0:
        
        data = list(range(1, 10001))
    else:
        data = None

    # Print the rank of the current process
    print(f"Parallel processing -> Process number: {rank} of {size-1} processes")
    # Broadcast the data to all processes
    data = comm.bcast(data, root=0)
    
    # Split the data into chunks for each process
    data_per_process = len(data) // size
    start_index = rank * data_per_process
    end_index = (rank + 1) * data_per_process if rank != size - 1 else len(data)
    local_data = data[start_index:end_index]
    
    # Calculate the partial sum of Fibonacci numbers
    local_sum = compute_partial_sum_of_fibonacci(local_data)
    
    # Gather all partial sums at the root process
    all_sums = comm.gather(local_sum, root=0)
    
    # If it's the root process, calculate the total sum
    if rank == 0:
        total_sum = sum(all_sums)
        
        # End timing
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        # Print the total sum and elapsed time
        print(f"Sum of Fibonacci Numbers: {str(total_sum)[:5]}...")
        print(f"Elapsed Time (Parallel): {elapsed_time:.4f} seconds")
