from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1:
            return True
        adj_list = collections.defaultdict(list)

        for want, need in prerequisites:
            adj_list[need].append(want)
        
        seen = set()
        def canTake(course):
            if course in seen:
                return False
            if not adj_list[course]:
                return True
            seen.add(course)
            for other in adj_list[course]:
                if not canTake(other):
                    return False
            seen.remove(course)
            adj_list[course] = []
            return True

        for course in range(numCourses):
            if not canTake(course):
                return False

        return True
