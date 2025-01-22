class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 1:
            return prerequisites[0][::-1]
        adj_list = collections.defaultdict(list)
        for course, pre in prerequisites:
            adj_list[pre].append(course)

        def dfs(course):
            if course in visited:
                return False
            if not adj_list[course]:
                return True
            
            visited.add(course)
            for oc in adj_list[course]:
                dfs(oc)
            visited.remove(course)
            adj_list[course] = []
            return True
        res = []
        visited = set()
        for course in range(numCourses):
            if dfs(course): 
                res.append(course)
            else:
                return []
        return res