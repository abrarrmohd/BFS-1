"""
Problem: Course Schedule
Approach: do a topolocgical sorting using BFS. Add elements to the queue only if indegree = 0
denoting that this node/element doesn't have any prerequisites anymore. In case of cycle,
not all the indegree values will be zero and the queue will be empty.
t.c. => O(V + E) 
s.c. => O(V + E) 
"""
from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0 for i in range(numCourses)]
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            inDegree[course] += 1
            graph[prereq].append(course)
        
        q = deque()
        for i in range(numCourses):
            degree = inDegree[i]
            if degree == 0:
                numCourses -= 1
                q.append(i)
    
        while q:
            node = q.popleft()
            for child in graph[node]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    numCourses -= 1
                    q.append(child)
        if numCourses > 0:
            return False
        return True
