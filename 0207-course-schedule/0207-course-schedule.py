class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time: O(#prereqs + numCourses)
        # Space: O(#prereqs + numCourses)
        pre_to_course = collections.defaultdict(list)

        for course, pre in prerequisites:
            pre_to_course[pre].append(course)
        
        visited = set()
        def dfs(course):
            if not pre_to_course[course]:
                return True
            
            if course in visited:
                return False
            
            visited.add(course)
            for c in pre_to_course[course]:
                if not dfs(c):
                    return False
            visited.remove(course)
            pre_to_course[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
