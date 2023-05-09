

# You are given a non-empty array of positive integers representing the time required to execute certain queries. Only one query can be run at a time, but queries can be run in any order. The wait time for a request is the specified amount of time it must wait before it starts. In other words, if the request is executed second, its waiting time is the duration of the first request; if the request is executed third, then its waiting time is the sum of the durations of the first two requests.

# Write a function that returns the minimum sum of the total waiting time for all requests. For example, if you receive requests with duration [1, , 5], the total waiting time if the requests were executed in order [5, 1, ] would be (0) (5) (5 1) = 11. The first request with a duration of 5 would be executed immediately, so the wait time would be 0, the second request with a duration of 1 would have to wait 5 seconds (the duration of the first request) before executing. , and the last request should wait the duration of the first two requests before executing.

# Note: You can change the input table.
# Sample Input

# queries = [3, 2, 1, 2, 6]
    

# Sample Output

# 17

def minimumWaitingTime(queries):
    queries.sort()
    
    total_waiting_time = 0
    
    for i in range(len(queries)):
        waiting_time = sum(queries[:i])
        total_waiting_time += waiting_time

    return total_waiting_time

print(minimumWaitingTime([3, 2, 1, 2, 6]))
print(minimumWaitingTime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(minimumWaitingTime([17, 4, 3]))
print(minimumWaitingTime([2, 1, 1, 1]))
print(minimumWaitingTime([25, 30, 2, 1]))
print(minimumWaitingTime([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))