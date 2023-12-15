#https://leetcode.com/problems/task-scheduler/discuss/3280549/Full-explanation-or-Using-Priority-Queue-and-Formula-based-Approach
import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap:
            cycle = n + 1
            remaining_tasks = []

            while cycle > 0 and max_heap:
                max_freq = -heapq.heappop(max_heap)
                if max_freq > 1:
                    remaining_tasks.append(max_freq - 1)
                time += 1
                cycle -= 1

            for count in remaining_tasks:
                heapq.heappush(max_heap, -count)

            if not max_heap:
                break

            time += cycle  # add idle time

        return time


sol = Solution()
tasks = ['A', 'A', 'A', 'B', 'B', 'C']
cooldown = 2
result = sol.leastInterval(tasks, cooldown)
print(result)