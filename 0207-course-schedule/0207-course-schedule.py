class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preHash = {i : [] for i in range(numCourses)}
        visit = set()

        for i in prerequisites:
            preHash[i[0]].append(i[1])

        def dfs(course):
            if course in visit:
                return False
            if preHash[course] == []:
                return True

            visit.add(course)
            for i in preHash[course]:
                if not dfs(i):
                    return False

            preHash[course] = []
            visit.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True