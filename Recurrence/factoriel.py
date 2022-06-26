import time


def factorielIterativf(n):
    if n == 0:
        return 0
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result


def factorielRecusif(n):
    if n == 1:
        return 1
    temp = factorielRecusif(n - 1)
    return temp * n


start_time = time.perf_counter_ns()
hit = factorielIterativf(999)
end_time = time.perf_counter_ns()
print(end_time - start_time)


start_time = time.perf_counter_ns()
n = factorielRecusif(900)
end_time = time.perf_counter_ns()
print(end_time - start_time)
