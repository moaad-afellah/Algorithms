import sys
import time


sys.setrecursionlimit(2000)


def sumRecursive(n):
    if n == 1:
        return 1
    temp = sumRecursive(n - 1)
    return temp + n


def sumIteratif(n):
    sum = 0
    for i in range(0, n + 1):
        sum = sum + i
    return sum


def sumDirect(n):
    return int(n * (n + 1) / 2)


start_time = time.perf_counter_ns()
sumRecursive(1500)
end_time = time.perf_counter_ns()
print(end_time - start_time)

start_time = time.perf_counter_ns()
sumIteratif(1500)
end_time = time.perf_counter_ns()
print(end_time - start_time)

start_time = time.perf_counter_ns()
sumDirect(1500)
end_time = time.perf_counter_ns()
print(end_time - start_time)