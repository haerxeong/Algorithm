import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])

    waiting_queue = []
    time = 0
    idx = 0
    total = 0
    count = len(jobs)

    while idx < count or waiting_queue:
        while idx < count and jobs[idx][0] <= time:
            request_time, running_time = jobs[idx]
            heapq.heappush(
                waiting_queue,
                (running_time, request_time, idx)
            )
            idx += 1

        if waiting_queue:
            running_time, request_time, job_num = heapq.heappop(waiting_queue)

            time += running_time
            total += time - request_time
        else:
            time = jobs[idx][0]

    return total // count