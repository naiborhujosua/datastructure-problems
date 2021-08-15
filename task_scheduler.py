"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq ={}
        for task in tasks:
            if task not in freq:
                freq[task] =1
            else:
                freq[task] +=1
        
        freq = [values for values in freq.values()]
        max_freq = max(freq)
        max_freq_tasks = freq.count((max_freq))

        # give values smallest than the length of our tasks
        result = (max_freq-1)*(n+1) + max_freq_tasks

        return max(len(tasks),result)

    #Formula
    ##(higher frequencies-1)(interval+1)(how many tasks with higher frequencies)
    