# Parallel and Distributed Computing with mpi4py

## Introduction

This project aims to provide a hands-on experience with parallel and distributed computing. We dive into the intricacies of parallel processing using the `mpi4py` library, a Python binding for the Message Passing Interface (MPI). By implementing and analyzing a Fibonacci sequence algorithm, we gain insights into parallelization's performance benefits and challenges.

## Context: Parallel Processing vs. Distributed Computing

- **Parallel Processing**: This involves executing multiple tasks or processes simultaneously, typically within a single machine. The primary goal is to speed up computation using multiple cores or processors.

- **Distributed Computing**: Tasks are distributed across multiple machines or nodes, each with local memory. These machines work together as a cluster to solve a problem. Distributed computing not only speeds up computation but also allows for the processing of large datasets that might not fit into the memory of a single machine.

## About mpi4py

`mpi4py` stands for MPI for Python, providing Python bindings for the Message Passing Interface (MPI). MPI is a standardized and portable message-passing system designed to allow processes to communicate in a parallel computing environment.

## Installation

To use `mpi4py`, you first need to install MPI. For this project, I used [Open MPI](https://www.open-mpi.org/).

Once MPI is installed, you can easily install `mpi4py` using pip:

```bash
pip install mpi4py
```

## Running the Code

To execute the sequential version of the Fibonacci sequence algorithm:

```bash
python3 main.py
```

For the parallel version, use:

```bash
mpiexec -n 12 python pararell_processing.py
```

Here, `-n 12` indicates that we're using 12 processes, instructing MPI to spawn 12 separate processes to run our Python script in parallel. Here's what happens behind the scenes:

> I used 12 processes because my machine runs a 12-core CPU (MacBook Pro M2).

### 1. Process Initialization:

MPI starts by initializing 12 separate processes. Each process will run the same Python script (`pararell_processing.py`). However, they each have a unique identifier called a "rank," which allows them to execute different parts of the code based on their assigned rank.

### 2. Data Distribution:

In our code, the root process (rank 0) initializes the data, a list of numbers from 1 to 10,000. This data is then broadcasted to all other processes using the `comm.bcast()` function. This ensures that every process has access to the entire dataset.

### 3. Workload Division:

Although every process has an entire dataset, each process doesn't compute the Fibonacci sum for the whole dataset. Instead, the dataset is divided into chunks, with each process responsible for a specific chunk. This division is based on the rank of the process. For instance, if we have 12 processes and 10,000 numbers, each process will handle 1,000 numbers.

### 4. Parallel Computation:

Each process computes the Fibonacci sum for its assigned chunk of data independently and in parallel with the other processes. This is where the magic of parallel processing shines, as multiple computations are happening simultaneously, significantly reducing total execution time.

### 5. Gathering Results:

Once all processes have computed their partial sums, the results are returned to the root process using the `comm.gather()` function. The root process then aggregates these partial sums to obtain the final result.

### 6. Final Output:

The root process (rank 0) prints the final aggregated sum and the total time for the parallel computation. The individual processes also print their rank, giving insight into the similar execution flow.

### Behind the Scenes:

Under the hood, MPI handles the communication between processes, ensuring data integrity and synchronization. It takes care of the complexities of inter-process communication, allowing us to focus on the algorithm and parallelization logic. MPI provides a seamless parallel computing environment by efficiently utilizing multiple cores or processors of a machine.

## Code Logic

The Fibonacci sequence algorithm calculates the sum of Fibonacci numbers for a list of numbers. In the sequential version, the algorithm processes the entire list in a single thread. In contrast, the parallel version divides the list among multiple processes, each calculating a partial sum. The root process (process 0) aggregates these partial sums to get the final result.

## Performance Analysis

From the results:

```
Running a sequential process...
Sum of Fibonacci Numbers: 88083...
Elapsed Time: 6.9102 seconds

Parallel processing -> Process number: 2 of 11 processes
Parallel processing -> Process number: 4 of 11 processes
Parallel processing -> Process number: 5 of 11 processes
Parallel processing -> Process number: 8 of 11 processes
Parallel processing -> Process number: 10 of 11 processes
Parallel processing -> Process number: 3 of 11 processes
Parallel processing -> Process number: 11 of 11 processes
Parallel processing -> Process number: 1 of 11 processes
Parallel processing -> Process number: 9 of 11 processes
Parallel processing -> Process number: 7 of 11 processes
Parallel processing -> Process number: 6 of 11 processes
Parallel processing -> Process number: 0 of 11 processes
Sum of Fibonacci Numbers: 88083...
Elapsed Time (Parallel): 1.6121 seconds
```

The parallel version is significantly faster. By distributing the workload across multiple processes, we substantially reduce execution time. This showcases the power and efficiency of parallel processing.

## Conclusion

Parallel processing offers a promising avenue for speeding up computational tasks. By leveraging the capabilities of `mpi4py` and MPI, we can efficiently distribute tasks across multiple cores or processors, leading to faster computations. However, it's essential to ensure correct parallelization and handle potential challenges like data synchronization and load balancing.
